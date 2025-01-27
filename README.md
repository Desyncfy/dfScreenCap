# DiamondFire Screen Cap

This project seems kind of insane but we have the technology

I do not recommend using this, as it's a bit of a mess, but:

## Tutorial
> [!WARNING]
> Intended only for people who actually know what they're doing (don't show up and ask me how to install git or something)

1. **Installing**

Clone this project and its submodules with
```bash
git clone --recursive https://github.com/Desyncfy/dfScreenCap.git
```
Next install the libraries with requirements.txt.
```bash
pip install -r requirements.txt
```
It has most of the libraries, but you'll probably need to install a few more. If you're on NixOS, use the shell.nix and requirements.txt in a virtual environment. (good luck)

2. **Running**

Install [CodeClient](https://github.com/DFOnline/CodeClient), enable ccapi. run the code. type /auth in your game and with any luck a countdown will appear and at the end it won't crash. Great. Now write some dfcode to interpret it or take mine:


## DFCODE
> [!IMPORTANT]
> This code is resolution dependent
```dfcode
1. {components:{"minecraft:custom_data":{PublicBukkitValues:{"hypercube:codetemplatedata":'{"author":"Chickenmanfy","name":"&e&lEvent &6» &ePlayer Join Game Event","version":1,"code":"H4sIAAAAAAAA/8VUXU/CMBT9K+Q+L0s3GGN7U6IxGqNR44sxpHQXbCzr0hURzf67txsKSOZ34tN2v07Pufe2zzBWWtyXkN48g8wgbWzwVt8U8AFzSzY3U8qiJIszl35bkU9YqXNKOtYyh8prgSgUX6IZrbJ3oZq/2uPKqYqSMm557Sr3G5gJVyV6dZTcj5AGPT/qsiAehMFgwOIg7HqwhDRiPvPgieKhn0TdMGJJHMT9QRSEHhTSijtIe36/lySJK+ALyowTP2aM9auKVJVKW0hZLWeT11iNLJ9uUNPFSv6ho0YBF07hBLHoXCMRlXYJG126QoWFNra1NevTw+h3xw/nxtDcOhfa8teu/4RGv9qa81tp66zlZNSAfT7ndkFni7wGaASdo5nJsnyn4oiXW4FdAu0ytmvXWgwX9+j6kkmDggqJEjpwuyyQrFyb2c/XfIvC0CAN5gFPdYYfMhBKN8P9CgV0i/AvevYy907MzR8L+ubT0b5SBzkfq/Ul2VNKLzqHSk7v7OZWXaKtQ2+R796QdwCtwgRXajSZ56KlsY0AyFBQPy8tbQt16bZ6AVbASKiwBQAA"}'}},"minecraft:custom_name":'{"extra":[{"bold":true,"color":"yellow","italic":false,"obfuscated":false,"strikethrough":false,"text":"Event ","underlined":false},{"bold":false,"color":"gold","italic":false,"text":"» "},{"color":"yellow","italic":false,"text":"Player Join Game Event"}],"text":""}'},count:1,id:"minecraft:ender_chest"}

2. {components:{"minecraft:custom_data":{PublicBukkitValues:{"hypercube:codetemplatedata":'{"author":"Chickenmanfy","name":"&b&lFunction &3» &bdecodeStream","version":1,"code":"H4sIAAAAAAAA/81YUW/aMBD+K8jP0QTtqLS8rWu7Vpq6arDtYa2QcY5g4djIvrSwKv99toE2EBJCQ9s9kdi+7+4+f76ceSRDodjEkPDPI+ERCRfvJFj+hmSUSmZfqY7tIrsGIVmutk9+xFmNuUS7KqJIn8acJXIlSZYFxAiFJDzqZsGG5VAMkMY5WzX1RiG5oMKAnXDTIbkyrUseRSBdMGy5JJpLmnC2GW7O4Ul2l62wSQRMRdBDDTQhPpJtGWuYAsUtOTukJ9cXSsM96ByMpmwCngWugVnnNhUfLs6n8Ixb6pePBlNB5xZzJ93lpH1/kB5gQdoN6IQb46ZyoV9SszZRDKBAYIlt/eSl0hWUG8DBPa2R+GLRKmu7+R47jWPv2zDlnQkuIZdDuyC62HoTOaBlkJcKh1S3rrxvx6F2uCE5gxFNBeYgOwVImSbFyI7yTK4T+RXwGzf4i4oUXosYwzSAPHODe5DzIo47hew+C+GI7FMbd2l+sUUfLK125uhfckXGz5HHs4vB9Wk/PP7U7QZMpRLDTsCj8JYkNkSm6QjDobDyHDAlLSEItySrJMDGlndjThfBjlw9CvysHZ5Zyw/dgMxJ2PUPf5cDU45s7J7bdpI++KesSjl13XXaK4ed9skeHjeE1wP8AfH66a1bAesoZQLzxmq796eiQmy1UOrIf4McW9XPKRufS9TzA5b2Zsc4OsQB3ptSnGERJSinrjcVHO23lcv4tYiYNWahmsqaVb3zvlW9OQsVCBt1/IZqA9dpMlzrdA6aTvNqcZBNfedPdXMWKhDeflNXaP/Bxh6/78Yuvu61eXjj3mPf8nDUWIvH9XatnTP5uMel8cZatJhSOuKS4vP18cvTUKvvvtnrDZHtVf0Cs2Xby+9Ca4aHaXFf8TBVCrGmMioxavSZxT6KCbW45Jc0Ujstqi+WtuVHrcRu4reKsFvJcrkI+9z9pbKSXp8n0PopOeZF95v69804y8XmDV7A5F32D+h8y9DkEQAA"}'}},"minecraft:custom_name":'{"extra":[{"bold":true,"color":"aqua","italic":false,"obfuscated":false,"strikethrough":false,"text":"Function ","underlined":false},{"bold":false,"color":"dark_aqua","italic":false,"text":"» "},{"color":"aqua","italic":false,"text":"decodeStream"}],"text":""}'},count:1,id:"minecraft:ender_chest"}
```
