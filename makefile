all: build_configuration_whl build_adapter_whl

build_configuration_whl:
	mkdir dist\configuration

	xcopy /S /Y /I configuration dist\configuration
	xcopy /S /Y /I dist\configuration\setup.py dist

	del dist\configuration\setup.py

	cd dist && python setup.py bdist_wheel
	xcopy /Y /I dist\dist\configuration-*-py3-none-any.whl .
	
	rmdir /s /q dist

build_adapter_whl:
	mkdir dist\adapter

	xcopy /S /Y /I adapter dist\adapter
	xcopy /S /Y /I dist\adapter\setup.py dist

	del dist\adapter\setup.py

	cd dist && python setup.py bdist_wheel
	xcopy /Y /I dist\dist\adapter-*-py3-none-any.whl .
	
	rmdir /s /q dist