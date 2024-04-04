echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python "
conda create --prefix ./env python -y
echo [$(date)]: "activating env"
source activate ./env
echo [$(date)]: "intalling dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"