# tool
# Python 3.10: https://drive.google.com/file/d/1-PNdtbIVFUpo6pi8RJAGkovRW8Jz9U9S/view?usp=sharing
# Ozone Jlink: https://drive.google.com/file/d/1um2XMeeqVrluA7x6qWdEM6Fi-dvxP7P6/view?usp=sharing
# https://drive.google.com/file/d/1zUmQSWwDy1BDzhRutPvFbI3raQdl6tFV/view?usp=sharing

B1: 
+ Vào UserConfig.py và config lai đường dẫn theo máy tính của mình 
+ pref_general.xdm chỉnh sửa lại version eb  : mặc định là 28.0
+ pref_general.xdm sử dụng module nào thì thêm module đó vào
+ Nếu generate mutil variant thì copy file systemmod/PostBuildVariantsSelectable.arxml ở eb tresos vào folder test/EbProject/systemmod
B2:
+ Vào cmd ở hàm main.py 
B3:
+ chạy các cmdline sau:

python main.py eb     : mở eb tresos lên, config và lấy config bỏ vào folder FW_HuLa\test\test_Gpio\Gpio_TS_001\config
python main.py clean   : clean output 
python main.py generate  : generate eb tresos
python main.py compile  : compile code 
python main.py debug  : debug bằng Ozone
python main.py report : chạy report ra file html
python main.py run  : download code
