



::1st way
SET STARTDIR=C:\Users\p.doulgeridis\Desktop\niarxos\
CD %STARTDIR%
for /R %%f in (*.*) do echo "%%f"
CD ..

pause


