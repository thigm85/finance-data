
BUILD_DIR=build

build:
	mkdir $(BUILD_DIR)
	cp -r src/python/prices $(BUILD_DIR)/
	cp bin/get_current_data.py $(BUILD_DIR)/
	chmod +x $(BUILD_DIR)/get_current_data.py

clean:
	rm -fr $(BUILD_DIR)
