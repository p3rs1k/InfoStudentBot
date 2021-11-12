from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.student_keyboards import student_keyword, all_student_keyword1, all_student_keyword2
from keyboards.default.choice_person import person
from handlers.users import student_functionals

from loader import dp


@dp.message_handler(text="Студент")
async def get_person_student(message: Message):
    await message.answer(
        f"Ви вибрали {message.text}!\n"
        f"Оберіть наступний крок:\n",
        reply_markup=student_keyword
    )


@dp.message_handler(text="Зареєструватись")
async def registration_student(message: Message):
    await message.answer(
        f"Напишіть номер гуртожитку в форматі:\nномер-KPI:",
        reply_markup=ReplyKeyboardRemove(),

    )


@dp.message_handler(text=[str(i + 1) + "-KPI" for i in range(25)])
async def write_hostel_number(message: Message):
    await message.answer(
        f"Ви вибрали гуртожиток {message.text}: \n"
        f"Введіть номер кімнати у форматі Х-ХХ:\n"
        f"Або повторіть спробу!"
    )


@dp.message_handler(text="Продовжити без реєстрації")
async def continue_without_reg(message: Message):
    await message.answer(
        f"Виберіть нижче потрібний функціонал:",
        reply_markup=all_student_keyword1

    )


@dp.message_handler(text="Оплатити проживання")
async def hostel_pay(message: Message):
    await message.answer(
        student_functionals.hostel_pay,
    )


@dp.message_handler(text="Оплатити інтернет зв\'язок")
async def internet_pay(message: Message):
    await message.answer(
        student_functionals.internet_pay,
    )


@dp.message_handler(text="Онлайн прання")
async def online_washing(message: Message):
    await message.answer(
        student_functionals.online_washing,
    )


@dp.message_handler(text="Друк документів")
async def printing_documents(message: Message):
    await message.answer(
        student_functionals.printing_documents,
    )


@dp.message_handler(text="Процедура поселення")
async def settlement(message: Message):
    await message.answer(
        student_functionals.settlement,
    )


@dp.message_handler(text="Процедура виселення на літо")
async def eviction(message: Message):
    await message.answer(
        student_functionals.eviction,
    )


@dp.message_handler(text="Далі")
async def next(message: Message):
    await message.answer(
        f"{message.text}",
        reply_markup=all_student_keyword2

    )


@dp.message_handler(text="Назад")
async def back(message: Message):
    await message.answer(
        f"{message.text}",
        reply_markup=all_student_keyword1

    )


@dp.message_handler(text="На головну")
async def home(message: Message):
    await message.answer(
        f"{message.text}",
        reply_markup=person

    )


@dp.message_handler(regexp="(\d{1}|\d{2})-(\d{2})")
async def write_room_number(message: Message):
    room_num = message.text.split('-')
    await message.answer(
        f"Ви ввели кімнату {room_num[0][-2:] if int(room_num[0][-2:]) < 13 else room_num[0][-1]}-{room_num[1][:2]}:\n"
        f"Введіть прізвище та ім\'я:\n"
        f"Або повторіть спробу",
    )
