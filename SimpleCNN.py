import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        
        # First Convolutional Layer: 1 input channel (grayscale), 32 output channels, 3x3 kernel size
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)  # Maintain size 45x45
        self.relu1 = nn.ReLU()
        
        # First Max-Pooling Layer: 3x3 filter with stride 3, reducing size from 45x45 to 15x15
        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=3)
        
        # Second Convolutional Layer: 32 input channels, 64 output channels, 3x3 kernel size
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1)  # Maintain size 15x15
        self.relu2 = nn.ReLU()
        
        # Second Max-Pooling Layer: 3x3 filter with stride 3, reducing size from 15x15 to 5x5
        self.pool2 = nn.MaxPool2d(kernel_size=3, stride=3)
        
        # Flattening Layer: Converts 5x5x64 to a 1D vector of size 1600
        self.flatten = nn.Flatten()
        
        # Fully Connected (Dense) Layer: Input size 1600, Output size 1024
        self.fc1 = nn.Linear(in_features=5 * 5 * 64, out_features=1024)
        self.relu3 = nn.ReLU()
        
        # Dropout Layer: Apply dropout with a rate of 0.4
        self.dropout = nn.Dropout(p=0.4)
        
        # Final Fully Connected Layer: Input size 1024, Output size 32 (number of classes)
        self.fc2 = nn.Linear(in_features=1024, out_features=32)
    
    def forward(self, x):
        # Forward pass through the layers
        x = self.conv1(x)        # Convolutional layer 1
        x = self.relu1(x)        # ReLU activation
        x = self.pool1(x)        # Max-pooling layer 1
        
        x = self.conv2(x)        # Convolutional layer 2
        x = self.relu2(x)        # ReLU activation
        x = self.pool2(x)        # Max-pooling layer 2
        
        x = self.flatten(x)      # Flattening layer
        x = self.fc1(x)          # Fully connected layer
        x = self.relu3(x)        # ReLU activation
        x = self.dropout(x)      # Dropout layer
        
        x = self.fc2(x)          # Output layer
        return x

if __name__ == '__main__':
    # Example usage
    # Create a dummy input tensor with a batch size of 1 and a grayscale image of size 45x45
    input_tensor = torch.randn(1, 1, 45, 45)

    # Instantiate the model and print the output
    model = SimpleCNN()
    output = model(input_tensor)
    print("Output shape:", output.shape)  # Should be (1, 32) since there are 32 output classes
