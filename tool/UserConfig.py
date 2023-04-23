#======================================= Begin User Config ==========================
# Config Test
PRO_DIR = 'E:/FW_HuLa/tool'
MODULE = 'Gpio'
TEST_NAME = 'Gpio_TS_001'
TEST_NAME_DESCRIPTION = "Test gpio blynk led"
LIST_TC_OF_TS = ['Gpio_TC_001','Gpio_TC_002']
LIST_TC_DESCRIPTION = ['Test gpio blynk led pd13','Test gpio blynk led pd14']

# Generate
EB_DIR = "C:/EB/tresos"

# Compile
COMPILER_DIR = "C:/GCC_THO"
COMPILER = 'gcc'

# Execute
OZONE_FILE = "C:/Program Files/SEGGER/Ozone/Ozone.exe"
JLINK_INTERFACE = "USB" # IP  USB
JLINK_SERIAL_NUMBER = "59768862"  # If JLINK_INTERFACE = USB
JLINK_IP = "192.168.1.6" # If JLINK_INTERFACE = IP
DEVICE = "STM32F407VG"
DEBUGER_JTAG_SWD = "JTAG"
JLINK_LIBRARY = 'C:/Tool/Jlink/JLink/JLink_x64.dll'
JLINK_FILE = 'C:/Tool/Jlink/JLink/JLink.exe'
PYTHON_DIR = 'C:/Python310'
#======================================= End User Config ==============================


#======================================= End Read Only ==============================
# Generate
GENERATOR = "Eb_Tresos"
EB_TESTPROJECT = f'{PRO_DIR}/../test/EbProject'
# Compile
TEST_DIR = f'{PRO_DIR}/../test/test_{MODULE}'
OUTPUT_DIR = f'{PRO_DIR}/../output/{MODULE}/{TEST_NAME}/{COMPILER}'
SRC_FILES = []
# Execute
DEBUGER = 'ozone'
#======================================= End Read Only ==============================

