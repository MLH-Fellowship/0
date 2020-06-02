while getopts "fh" flag; do
    case "${flag}" in
        f)
        echo "Deleting existing 124M model"
        if [ -d "models/124M" ]; then
            rm -rf "models/124M"
        fi
        ;;
        h)
        echo "-h, show help"
        echo "-f, reinstall model 124M "
        exit 0
        ;;
        *) break;;
    esac
done

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
