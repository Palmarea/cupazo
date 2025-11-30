# cupazo
*hackatonAI2025*

# What am I?
A voice bot, help you out with a call.
- Using Qwen2-7B-Instruct model to answers.
- Text to voice using Eleven Labs TTS.

# Run me
### steps

Clone repository

```bash
git clone https://github.com/Palmarea/cupazo.git
```

### STEP 01- Create a conda environment after opening the repository

``` bash
conda create -n sabobot python=3.10 -y
```

``` bash
conda activate sabobot
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- API Key de Eleven Labs en -config/config.py-
in : python main.py

# Files Structure
```
asistente-voz/
├─ main.py
├─ config/
│ └─ config.py
├─ modules/
│ ├─ voice_input.py
│ ├─ voice_output.py
│ └─ assistant.py
└─ data/
└─ logs.txt
```
