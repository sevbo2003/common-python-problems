## Test yozishdan qochmang
***
Assalomu alekum. Ushbu maqolada **Test** yozish haqida gaplashamiz. Maqola muallifi [Akhmadiy](https://t.me/programming_everyone).

    print("Test yozish haqida")

## Testlar

Negadur ko'pchilik  testlarni yozishni xoxlamaydi. Kop kompaniyalarda esa umuman testing masalasiga etibor qaratilmaydi. Bu borada tanqidiy hulosalar ko'p ammo bularni xozircha bayon qilmoqchi emasman. Xozir Testlardan nima manfat ko'rganim shu bilan birga qanday tajribalar qilganimni bo'lishimoqchiman.

Testlar yozish masalasida eng avvalida integration va E2E testlardan boshladim taxminan 2 yil avval. Testlarni kop holatlarda talabga emas biror qilingan funksionalga qarab yozar edik. Xozirgacha kopchilik shunday o'ylasa kerak.

Ammo minde o'ylab qarasam bu umuman foydasiz ekan ))). Test yozish emas yondoshuv yoki uslub xato !

Keyin qarashlar va olchovlar o'zgarib (Shakillanib) boshladi. Testlar haqida shaxsiy fikrlar paydo bo'la boshlagandan keyin talablar ham paydo bo'ldi yoki borlari o'zgardi.

Keyin birqancha savollar qiynadi.
1. Testlar nima uchun kerak ? Test yozishda o'zi qanday yondoshuv kerak ?
2. Nima uchun Unit Testlar yozishim kerak axir Integration yoki E2E bundan ko'proq value beradiku !
3. Nima sababdan dasturchi test yozishi kerak buni ana testerlar qilgani yaxshi...
4. Client test yozganimga pul bermaydi ((
5. Xop test yozaman ammo nimani testlashim kerak ? Aynan qayerda test yozish keragu qayerda yo'q
6. Test yozish jarayonida mocking qilish g'alatiku. Mock functional bilan real ishlashdagi farqli bo'lishi mumkin

Bu savollarga javob topguncha ancha vaqt ketdi. Ammo javoblar xozircha qoniqtirdi va yangi savollar paydo bo'lmoqda ))).

Demak javoblar.

1. Testlash va testlar yozish ortiqcha ish emas. Biz testlarda aniq requirementlarni belgilab izohlay olsak testlar ishimizni ancha osonlashtiradi shu bilan birga qilingan ish yoki functional requirementga qanchalik mos kelishini isbotlay oladi. Shu sababdan testlarni aniq requirementlarga qarab yozishimiz kerak va bu o'ta muhim !

2. E2E va Integration testlar biror functionalni to'liq ishlayotganini tekshiradi. Yani barcha qismlar yaxlit qilib yeg'ilib bajaryaotgan ishini tekshiradi. Yani buyoqda jarayon abstract ammo natija muhim bo'ladi. (Jarayoni ham to'liq testlash mumkin ekani xaqida eshitganman ammo tajribada sinalgani yo'q xozircha)
Unit testlar esa aniq maqsadga qaratilgan kichik qismlarni tekshiradi. Shu bilan bir qatorda  Unit Testlar yozish orqali code yozishni ham o'rganvoman. Ayniqsa har Single Responsibilityga qattiq rioya qilish muhim. Bo'lmasa Unit Testlardan foyda yo'q. Agar codeda Unit Testlar bo'lsa va testable bo'lsa demak unday bo'lmaganidan ko'ra sifatli code bo'lish extimoli katta. Yani Unit Testlar bizga IDE darajasida muhim.

3. Testlarni dasturchi yozishi kerak. Chunki dasturchidan boshqasi qilgan ishiga javob bera olmaydi. Agar testlar yaxshi implement qilingan bo'lsa. Dasturchilar qilgan ishlarini testlar yordamida isbotlay oladilar (To'g'ri bu managementga umuman qiziq emas afsuski ). Ammo biz xatolarimizni clientdan yoki managerdan oldin topishimiz uchun ham test yozishimiz kerak. Testlar birinchi bug filter vazifasida ham bo'lishi mumkin.

4. To'g'ri client code yozganga pul to'laydi. Ammo clientga yozgan code aniq requirementlarga javob berayotganini isbotlash uchun ham testlar kerak. Buyoqda siz o'z ishingiz sifatini o'lchashingiz uchun ham test yozishiz kerak.

5. Testlashda eng muhim narsa testlar sizning qilgan ishingiz malum talablarga javob berish bermasligini aniqlash degan ekanmiz demak testlarni imkon qadar hamma joyda yozish kerak. Coreda ham oddiy kichik functionalarda ham. Yoki sodda bir maqsadli functionlarda ham.  API darajasida ham.
6. E2E yoki integration testlar uchun mocking mani nazarimda ham unchalik effektiv bo'lmaydi. Ammo Unit Testlarda mocking ishlatilishi mumkin. Masalan sizda test qilmoqchi bo'lgan biror class ichida biror qoshimcha dependency ishlatilgan deylik. Siz esa faqatgina o'sha class qanday ishlashini test qilmoqchisiz sizga classning boshqa dependencylar bilan birga ishlab keyin qaytaradigan natijasi emas sizga class aniq talablarga aniq javob berishi yoki bermasligi qiziq. Shu sababdan unga bogliq dependencylarga etibor qaratmaslik kerak. Siz aniq bir maqsada faqatgina bir functionalni test qilmoqchisiz. Keyin boshqa tomondan o'ylasak shunga o'xshash yondoshuv to'g'ridan to'g'ri codebaseni ham to'g'ri yozishga sabab bo'ladi. Yuqorida shu masalaga oxshash masalalardan yig'ilgan hulosalarim natijasida Testlash code yozishni o'rgatyabti degan edim. 

PS: Sifatli productning asosiy o'lchovlaridan biri bu xatolikga yo'l qo'ymaslik emas. Xatoliklarni productionga chiqishdan avval masimal bartaraf etish. Ushbu amaliyotda eng muhim jarayonlardan biri testing.

TDD haqida sal keyinroq )))