@echo off

call :treeproc
goto :eof

:treeproc
for %%f in (*.py) do (
	@echo %1/%%f
	sed -i "s#\"../../_inputs#\"_inputs#g" %%f
)
for /D %%d in (*) do (
	if not "%%d"=="_inputs" (
		cd "%%d"
		call :treeproc %1/%%~nd
		cd ..
	)
)
exit /b
