# corona virus stats for catuserbot
from covid import Covid

from . import covidindia


@bot.on(admin_cmd(pattern="كورونا(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="كورونا(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "**⌔∮ جاري جمع المعلومات. **")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⌔∮ الاصابات المؤكده : <code>{hmm1}</code>"
        data += f"\n⌔∮ الاصابات المشبوهه : <code>{country_data['active']}</code>"
        data += f"\n⌔∮ الوفيات : <code>{hmm2}</code>"
        data += f"\n⌔∮ الحرجه : <code>{country_data['critical']}</code>"
        data += f"\n⌔∮ حالات الشفاء : <code>{country_data['recovered']}</code>"
        data += f"\n⌔∮ اجمالي الاختبارات : <code>{country_data['total_tests']}</code>"
        data += f"\n⌔∮ الاصابات الجديده : <code>{country_data['new_cases']}</code>"
        data += f"\n⌔∮ الوفيات الجديده : <code>{country_data['new_deaths']}</code>"
        data += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
        await catevent.edit(
            "<b>𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𝑪𝑶𝑹𝑶𝑵𝑨 𝑰𝑵𝑭𝑶 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n ⌔∮ معلومات فايروس كورونا في - {} :\n{}</b>".format(
                country, data
            ),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𝑪𝑶𝑹𝑶𝑵𝑨 𝑰𝑵𝑭𝑶 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n ⌔∮ معلونات فايروس كورونا في - {data['state_name']} :\
                \n⌔∮ الاصابات المؤكده : <code>{data['new_positive']}</code>\
                \n⌔∮ الاصابات المشبوهه : <code>{data['new_active']}</code>\
                \n⌔∮ الوفيات : <code>{data['new_death']}</code>\
                \n⌔∮ حالات الشفاء : <code>{data['new_cured']}</code>\
                \n⌔∮ اجمالي الاختبارات  : <code>{cat1}</code>\
                \n⌔∮ الحالات الجديده : <code>{cat2}</code>\
                \n⌔∮ الوفيات الجديده : <code>{cat3}</code> </b>\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
            await catevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                catevent,
                "**⌔∮ معلومات فايروس كورونا في - {} غير متوفره !**".format(country),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n  •  **Syntax : **`.covid <country name>`\
        \n  •  **Function :** __Get an information about covid-19 data in the given country.__\
        \n\n  •  **Syntax : **`.covid <state name>`\
        \n  •  **Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
