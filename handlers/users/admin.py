from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default.admin_keyboards import registration, admin_panel, to_home
from keyboards.default.choice_person import person

from loader import dp


@dp.message_handler(text="Адміністратор")
async def get_person_admin(message: Message):
    await message.answer(
        f"Ви вибрали роль {message.text}!\n"
        f"Нажміть на клавішу авторизації",
        reply_markup=registration
    )


@dp.message_handler(text="Авторизуватись")
async def registration_admin(message: Message):
    await message.answer(
        f"Напишіть номер гуртожитку в форматі:\nномер/KPI:",
        reply_markup=to_home
    )


@dp.message_handler(text=[str(i+1) + "/KPI" for i in range(25)])
async def choice_hostel(message: Message):
    await message.answer(
        f"Ви вибрали гуртожиток {message.text}: \n"
        f"Введіть пароль для авторизації: ",
        reply_markup=to_home
    )


@dp.message_handler(text=["qwerty", "password"])
async def send_password(message: Message):
    await message.answer(
        f"Авторизація пройшла успішно.\n"
        f"Виберіть нижче потрібний функціонал:",
        reply_markup=admin_panel
    )


@dp.message_handler(text="Знайти студента")
async def find_student(message: Message):
    await message.answer(
        f"Введіть прізвище та ім'я студента.\n",
    )


@dp.message_handler(text="Написати студентам з кімнати")
async def write_to_room(message: Message):
    await message.answer(
        f"Введіть кінмату у форматі Х/ХХ.\n",
    )


@dp.message_handler(regexp="(\d{1}|\d{2})/(\d{2})")
async def write_to_roommates(message: Message):
    room_num = message.text.split('/')
    await message.answer(
        f"Введіть текст, який ви хочете надіслати мешканцям кімнати: "
        f"{room_num[0][-2:] if int(room_num[0][-2:]) < 13 else room_num[0][-1]}-{room_num[1][:2]}.\n"
        f"Або повторіть спробу",
    )



@dp.message_handler(text="Розіслати усім")
async def write_to_all(message: Message):
    await message.answer(
        f"Введіть текст, який ви хочете розіслати усім мешканцям гуртожитку.\n",
    )


@dp.message_handler(text="На головну")
async def get_back(message: Message):
    await message.answer(
        "Виберіть сценарій: ",
        reply_markup=person
    )

@dp.message_handler(lambda message: len(message.text) <= 25 and len(message.text.split()) <=3, regexp="[\w\`]+\s[\w\`]+")
async def write_name(message: Message):
    await message.answer(
        f"Ви ввели:\n{message.text}",
        reply_markup=person
    )

@dp.message_handler(lambda message: len(message.text) > 15)
async def text_to_roommates(message: Message):
    await message.answer(
        f"Текст надіслано отримувачам"
    )