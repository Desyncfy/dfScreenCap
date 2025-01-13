# DiamondFire Screen Cap

This project seems kind of insane but we have the technology

I do not recommend using this, as it's a bit of a mess, but:

## Tutorial
1. **Installing** <br> Clone this project and its submodules, requirements.txt has most of the libraries, but you'll probably need to install a few more. If you're on NixOS, use the shell.nix and requirements.txt good luck there.
2. **Running** <br> install [CodeClient](https://github.com/DFOnline/CodeClient), enable ccapi. run the code. type /auth in your game and with any luck a countdown will appear and at the end it won't crash. Great. Now write some dfcode to interpret it or take mine:


## DFCODE
```json
1. {components:{"minecraft:custom_data":{PublicBukkitValues:{"hypercube:codetemplatedata":'{"author":"Chickenmanfy","name":"&e&lEvent &6» &ePlayer Join Game Event","version":1,"code":"H4sIAAAAAAAA/7VSTWsCMRD9KyVnTz30kJuUllIoLXgUWWIyboOzyZKMisj+9042i3Vbox7aUzJfb94b3kEs0et1FHJ+ENYImWMxGV4pYAuOOFah5i5uImhS+6LjnCbrHTe9eutENylA2FXVotpDOAOTf30mj1akau4zilTK+nZY8b5zPUAqS/EBobExptIJjRcVR4XfBDpmHdGTkPcP3UjCePZbS1B6DekAxgbQPMiUIIHTvgWOnA9NWXpeWw1brlzxMYAiu4U3b+AiA40+wq0UAONltH/TMzXJO5vwx4KucbjZUk9OLRGOnpoi+t3dM9r6k05dNQPqS8fKeSJla/0AKArTCrFabZwuHDYLEAY033NG7Ba+0qL7At64dKXEAwAA"}'}},"minecraft:custom_name":'{"extra":[{"bold":true,"color":"yellow","italic":false,"obfuscated":false,"strikethrough":false,"text":"Event ","underlined":false},{"bold":false,"color":"gold","italic":false,"text":"» "},{"color":"yellow","italic":false,"text":"Player Join Game Event"}],"text":""}'},count:1,id:"minecraft:ender_chest"}

2. {components:{"minecraft:custom_data":{PublicBukkitValues:{"hypercube:codetemplatedata":'{"author":"Chickenmanfy","name":"&b&lFunction &3» &bdecodeStream","version":1,"code":"H4sIAAAAAAAA/+1Y3W/aMBD/V6I8o6nQsoe8dWu7VuqXBtsepgoZ5whWHTuynQ5W5X+f7QA1+YIUWDtpTyT23e/ufne+nHn2x5TjR+kHP599EvpB/u53Fr+BP0kZ1q9IRFpIyyiIF9L6ya4YrSlhSkuFSKHVmtFUhDM/yzq+pFz5Qa+fdQqaYzpSKHJ0eWKVAv8CUQl6w2wH/pX0LkkYAjPO4IVIOGcoJrjormPwY/aQLbH9EDAPYaAEoNi3nlRFLCABpCpiNkgr0xdcwBMIB0Yg/AiWBSIAa+M6FOuumifwgltrl0xGCUVzjbmR7nrS7iYTb4pYuOLtUr94A0OG4/yVvOQ0JCyqNF+ir1IPKSXIOFUmtNu7YQsiGBcN9EtQoye0BQm50JIBXQgGW2IBwM7Mog4Cc2uQEgZOVEelIoy0ReqALRw1ZFr+roywYVREYOI5gwlKqXIwu+tEfQF1SqlRGyIdRG2wOeOjhd7GkDGPk3LMEEXdxvDqy2UoUueIsSkIoryBmlOQbr0MgIU3ICWKoNZ5p2pOWnhwGoaeTBC2BnM/hjBT3ndEU/BuQESLcnulL206zleIUmqrKnfklJKIxcCUd6P7xg5OFI6Rq92+DW1zDB5h3qb+KzGeTAbqUbrboWxzIHtZsbWeIzw9Z0rM99hfd2ssYcuWsh9K1UyVUTr11A0SSpT+wJkzcyAiZjuz0ExlmQSWxmWQbj0JuvleE6lsB3m/LDQgFD4m90hIuE3j8dq4sddwdu8We0lq722TujsLDQh/P6lLtHeQ2OO3TawGacNDLr66zMhPuRMTcyHp2F29PNOaH/odnfKgbx9+Lx8SovDU7B7pXfTLPmWtP5wN/aG3czEeb5e2/pGj02aqu9caHuZc6MsCUi8j5ufVkjc0X+21ociMzFZAViS+aZpyFA87aV9zHLQ/QY3VV66G/9P6PzitRzrVWxfXAbt1y1prj1EcOEHpPFgCGwZ1THn+V07NpL5Ro/kvA8z1VYHTzcRXNrmTV96dB6Dths5BIDF43xhZ+6flB7LvRU/rq80qvILLh+wPLL4J1swTAAA="}'}},"minecraft:custom_name":'{"extra":[{"bold":true,"color":"aqua","italic":false,"obfuscated":false,"strikethrough":false,"text":"Function ","underlined":false},{"bold":false,"color":"dark_aqua","italic":false,"text":"» "},{"color":"aqua","italic":false,"text":"decodeStream"}],"text":""}'},count:1,id:"minecraft:ender_chest"}
```
