# Manual Checker (th)

## คำแถลง

สิ่งนี้เป็นผลงานของข้าพระเจ้า **มิอนุญาติ** ให้ปรับแต่หรือการกระทำอื่นใดที่นอกจากเป้าประสงค์ของข้าพระเจ้า หากมีข้อสงใสกรุณาอ่านไฟล์ `LICENCE` และ `EULA`

## ปัจฉิมลิขิต
หากท่านใช้สิ่งนี้แล้วถือว่าท่านยอมรับใน ข้อตกลงข้อตกลงอนุญาตให้ใช้สิทธิของผู้ใช้ ("EULA : End User License Agreement") หากมีข้อสงใสกรุณาอ่านใน `EULA`

## การตั้งค่า
เมื่อท่านสังเกตุเห็นไฟล์ `.env` นั้นคือไฟล์ที่จะกำหนดคุณลักษณะในการใช้งานสิ่งนี้อย่างเต็มประสิทธิภาพ

```
OUTPUT_SEQUENCE_JSON=sequence.json
INPUT_SEQUENCE=sequence
RAR_REGEX=\d{4}_?.*\w(?=.rar)
```

>`OUTPUT_SEQUENCE_JSON` ตำแหน่งสำหรับนำไฟล์ที่อยู่ในรูปแบบที่สิ่งนี้สามารถนำไปใช้ได้

>`INPUT_SEQUENCE` ตำแหน่งสำหรับบอกสิ่งนี้นำไฟล์ที่ท่านเขียนไปอยู่ในรูปแบบที่สามารถอ่านได้

>`RAR_REGEX` สำหรับการจับไฟล์ที่ท่านต้องการให้สิ่งนี้ตรวจสอบ ณ ขนานนี้สิ่งนี้รองรับแค่ไฟล์นามสกุล `.rar` เท่านี้น

### การเขียนข้อกำหนดในการทาน

ในไฟล์ตัวอย่างได้รวบรวมความสามารถทุกอย่างไว้แล้ว
```
CASE 1: html > body > table @ width = "1024";
CASE 2: * table @ width = "1024";
CASE 3: * div > table @ width = "1024";
CASE 4: html > body > table;
```

**สำคัญมาก**: เนื่องจากสิ่งนี้มีการทานสิ่งที่ท่านเขียนหากไม่ถูกต้องจะมีข้อความบอกท่านดังนี้

```bash
Illegal character at position {อักขระที่ผิดพลาด}
```

## รูปแบบไวยากรณ์ (Syntax)
```
CASE {A} : * {\s_1} > {\s_2} > {\s_3}... > {\s_n} @ {B} = {C};
```

|สัญลักษณ์|ความหมาย|
|:-:|:-:|
|CASE|เป็นการระบุจุดเริ่มต้นของกระบวณการ|
|A|เป็นตัวเลขลำดับสำหรับความอ่านง่ายของท่าน|
|:|เป็นจุดเริ่มต้นสร้างเงื่อนไข|
|*|เป็นการบอกว่าหาจากจุดไหนก็ได้|
|\s_{1~n}|หมายถึงข้อความที่ท่านต้องการให้ตรวจ|
|>|เป็นการระบุว่ามีข้อความต่อไป|
|@|เป็นจุดเริ่มต้นว่าสิ่งที่จะหาจำเป็นต้องมีตัวแปลนี้|
|B|ชื่อของตัวแปร|
|=|กำหนดค่าของตัวแปร|
|C|ค่าของตัวแปร|
|;|เป็นการระบุจุดสิ้นสุดของกระบวนการ A|

## รูปแบบการใช้งาน

หลังจากทำขั้นตอนก่อนหน้าแล้วสามารถนำไปใช้ได้โดย

```bash
python3 main.py -c
python3 main.py -i {ตำแหน่งเป้าหมาย}
```

> `-c` หมายความว่าให้แปลจาก `INPUT_SEQUENCE` ไป `OUTPUT_SEQUENCE_JSON`

> `-i` หมายถึงบอกสิ่งนี้ว่าเราจะระบุตำแหน่งเป้าหมายให้ หากไม่ระบุจะไม่สามารถทำการกระทำต่อไปได้ **โปรดระวัง**