# Computer Vision-based Math Solver

## Project Overview
This project focuses on building a Computer Vision-based Math Solver aimed at recognizing mathematical symbols and solving equations from handwritten or printed math expressions. By using a lightweight model, this project achieves improved accuracy and efficiency in character recognition, tailored for school-level mathematics.

---

## Features
- **Lightweight Custom CNN Model**: Designed to efficiently recognize 128 distinct mathematical symbols.
- **Sliding Window Approach**: Captures individual symbols from complex mathematical expressions for accurate detection.
- **Preprocessing Steps**: Includes grayscale conversion, inversion, and text rectification to handle irregular text layouts.
- **Math Expression Solver**: Combines detected symbols into coherent mathematical expressions for further processing.

---

## Dataset
- **Source**: The CROME dataset, converted from InkML to PNG format.
- **Classes**: 128 symbols covering digits, operators, trigonometric functions, and Greek letters.
- **Data Distribution**: Approximately 12,800 images, with 100 samples per symbol on average.

---

## Model Architecture
The framework is built upon a simplified version of EasyOCR:
1. **Convolutional Layers**: Extract features from input images.
2. **ANN Layers**: Predict label distributions for each symbol (replacing traditional RNN layers for efficiency).
3. **Transcription Layer**: Converts per-frame predictions into final label sequences.

### Key Innovations
- Sliding window approach for symbol detection.
- Thin Plate Spline (TPS) transformation for text rectification.
- Handling of subscripts, superscripts, and multi-line expressions using positional information.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Ranjan00001/MathSolver.git
   cd MathSolver
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and prepare the dataset (instructions provided in the `dataset` folder).

---

## Challenges and Solutions
### Challenges
1. Variability in handwritten symbol sizes and styles.
2. Computational overhead of sliding window processing.
3. Context-dependent symbols (e.g., subscripts and superscripts).

### Solutions
- Adaptive window sizing for symbols of varying dimensions.
- Batch processing to speed up CNN inference.
- Post-processing rules for handling positional information in mathematical expressions.

---

## Future Work
1. Extend the symbol set to include advanced mathematical notations.
2. Implement an end-to-end solver for parsing and solving equations.
3. Optimize the model for mobile and edge devices.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributors
- **Deependra Shukla**
- **Nagmani Kumar**  
- **Ranjan Singh**
