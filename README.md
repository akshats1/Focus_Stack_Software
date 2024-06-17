# Focus_Stack_Software
Gui Made using PyQT
## How to Run
```bash
conda create -n focussoft python=3.8 -y
```
```bash
conda activate focussoft
```
```bash
pip install -r requirements.txt

```

### Go to src directory
```bash
cd src/

```


```bash
python3 run.py

```

### Folder Sctructure 

├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── src
    ├── algorithms
    │   ├── API.py
    │   ├── dft_imreg.py
    │   ├── __init__.py
    │   ├── ProgressLoggingHandler.py
    │   └── stacking_algorithms
    │       ├── cpu.py
    │       ├── gpu.py
    │       └── __init__.py
    ├── ImageLoadingHandler.py
    ├── __init__.py
    ├── MainWindow
    │   ├── ImageSavingDialog.py
    │   ├── __init__.py
    │   ├── MainLayout
    │   │   ├── ImageViewers
    │   │   │   ├── ImageRetouchScene.py
    │   │   │   ├── ImageScene.py
    │   │   │   ├── __init__.py
    │   │   │   └── RetouchHelpers.py
    │   │   ├── ImageWidgets.py
    │   │   └── __init__.py
    │   ├── ProgressBar.py
    │   ├── QActions.py
    │   ├── SettingsWidget.py
    │   ├── StackSuccessDialog.py
    │   ├── Threading.py
    │   └── TimeRemainingHandler.py
    ├── run.py
    ├── settings.py
    └── utilities.py

6 directories, 30 files
