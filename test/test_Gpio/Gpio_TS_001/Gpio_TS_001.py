SRC_DIRS =[
    f'{PRO_DIR}/../driver/{MODULE}/source',
    f'{PRO_DIR}/../env/source',
    f'{TEST_DIR}/{TEST_NAME}/src'
]

for TC in LIST_TC_OF_TS:
    SRC_DIRS.append(f'{TEST_DIR}/{TEST_NAME}/{TC}/src')

INCLUDE_DIRS = [
    f'{PRO_DIR}/../driver/{MODULE}/include',
    f'{PRO_DIR}/../env/include',
    f'{TEST_DIR}/{TEST_NAME}/include'
]
for TC in LIST_TC_OF_TS:
    INCLUDE_DIRS.append(f'{TEST_DIR}/{TEST_NAME}/{TC}/include')

XDM_FILES = [
    f'{TEST_DIR}/{TEST_NAME}/Config_Xdm/Port.xdm',
    f'{TEST_DIR}/{TEST_NAME}/Config_Xdm/Resource.xdm'
]