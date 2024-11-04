# Setting Up Rasa Virtual Environment

This guide will help you create and set up a virtual environment for Rasa.

## Step 1: Create a Virtual Environment
Run the following command in your terminal:

```bash
python3.10 -m venv rasa_env
```

## Step 2: Activate the Virtual Environment

After creating the virtual environment, activate it using one of the following commands:


```bash
  source rasa_env/bin/activate
```

## Step 3: Install Rasa

Once the virtual environment is activated, you can install Rasa using pip:


```bash
pip install rasa
```


## Step 4: Train Your Model

If you already have a Rasa project with training data, you can train your model by navigating to your project directory and running:

```bash
rasa train
```

## Step 5: Run the Rasa Server

Once your model is trained, you can run the Rasa server:

To run the Rasa Action Server (if you have custom actions): In one terminal window, run:

```bash
rasa run actions
or

rasa run -m models --enable-api --cors "*"


```

