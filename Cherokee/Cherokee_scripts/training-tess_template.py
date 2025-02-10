import subprocess

# Paths to required files
output_dir = r"G:\Cherokee\ltmsf"
traineddata_path = r"G:\Cherokee\chr.traineddata"
model_output = r"G:\Cherokee\output\checkpoints\cherokee"
lstm_model_path = r"G:\Cherokee\chr.lstm"
train_listfile = r"G:\Cherokee\output\training_files.list"
eval_listfile = r"G:\Cherokee\output\eval_files.list"

# Command to run lstmtraining
command = [
    "lstmtraining",
    f"--model_output={model_output}",
    f"--traineddata={traineddata_path}",
    f"--train_listfile={train_listfile}",
    f"--eval_listfile={eval_listfile}",
    f"--continue_from={lstm_model_path}",
    "--max_iterations=10000",
    "--debug_interval=100",
    "--learning_rate=0.002"
]

print("Executing command:", " ".join(command))

try:
    subprocess.run(command, check=True)
    print("Training completed successfully!")
except subprocess.CalledProcessError as e:
    print(f"Training failed with error: {e}")
