# Digit Recognition using Neural Network and Pygame
This repository provides a digit recognition system using a neural network and Pygame. The system allows users to draw digits on a drawing board using a cursor, and the neural network then detects and outputs the recognized digit in text form.

<img src="https://i.imgur.com/79trBEu.png" width="400" height="300"> <img src="https://i.imgur.com/Mx9XBSC.png" width="400" height="300"> <img src="https://i.imgur.com/WA1viq9.png" width="400" height="300">


## Requirements
To run this digit recognition system, you need to have the following:
- Python 3.x
- Pygame library
- Numpy library
- Keras library

## Installation
1. Clone the repository:
2. Change into the project directory:
3. Install the required dependencies:

## Usage
To use the digit recognition system, follow these steps:
1. Run the application:
2. A Pygame window will open, displaying a drawing board.
3. Use the cursor to draw a digit (0-9) on the drawing board.
4. Press the "Recognize" button to let the neural network detect the drawn digit.
5. The recognized digit will be displayed in the output text box.

## Model Training

The neural network model used for digit recognition is trained using the MNIST dataset. To train the model yourself or retrain it with custom data, follow these steps:

1. Prepare your training data, ensuring it is in the same format as the MNIST dataset (28x28 pixel images).
2. Modify the `train_model.py` file to load your custom training data.
3. Run the training script:
4. The model will be trained on your data and saved as `himanshhu.h5`.
   
## Acknowledgements
We would like to express our gratitude to the open-source community for their invaluable contributions and the various libraries, frameworks, and datasets that have made this project possible.

## Contact
For any inquiries or feedback, please contact us at himanshuhiware071@gmail.com.
