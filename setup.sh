python -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Downloading model..."
python download_model.py 124M
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
