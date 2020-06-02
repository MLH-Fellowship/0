python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Downloading model..."
if [ ! -d "models/124M" ]; then
    python download_model.py 124M
else
    echo "Model 124M already exists"
fi
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
