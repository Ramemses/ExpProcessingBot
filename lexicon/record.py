from math import sqrt

direct_record_lexicon = {
    "help_message": (
        "Для получения результатов по прямым измерениям\n"
        "нужно отправить следующие значения:\n\n"
        "• кол-во измерений (сколько раз измерялась данная физическая величина)\n"
        "• сами значения измерений через запятую\n"
        "• приборную погрешность (если такова имеется. Обычно обозначается \"Θ\")\n\n"
        "Данные отправлять в следующем формате:\n"
        "```\n"
        "n\n"
        "x1, x2, x3, ...\n"
        "Θ\n"
        "```\n"
        "*Пример:*\n"
        "```\n"
        "5\n"
        "10.5, 10.7, 10.4, 10.6, 10.5\n"
        "0.1\n"
        "```\n"
        "*(Если приборной погрешности нет, просто отправьте первые две строки)*\n\n"
        "В качестве ответа я предоставлю полное описание расчета погрешностей"
        "правильно оформленное для обработки"
    ),


}



def get_avarage_message(record_count: int, records: list[float], result: float) -> str:
    return (
        "📊 **Расчет среднего арифметического**\n\n"
        
        "**Исходные данные:**\n"
        f"• Количество измерений: `{record_count}`\n"
        f"• Значения: `{', '.join(f'{x}' for x in records)}`\n\n"
        
        "**Формула:**\n"
        "```\n"
        f"x̄ = (∑xᵢ) / n\n"
        f"   = ({' + '.join(f'{x}' for x in records)}) / {record_count}\n"
        "```\n\n"
        
        "**Вычисления:**\n"
        f"• Сумма: `{sum(records)}`\n"
        f"• Деление на `{record_count}`\n\n"
        
        "🎯 **Результат:**\n"
        f"```\n"
        f"x̄ = {result:.6f}\n"
        "```"
    )


def get_rms_message(record_count: int, avarage: float, sum_squared: float, result: float):
    return (
        "📈 **Расчет стандартного отклонения (СКО)**\n\n"
        
        "**Исходные данные:**\n"
        f"• Количество измерений: `{record_count}`\n"
        f"• Среднее значение: `{avarage:.6f}`\n\n"
        
        "**Формула:**\n"
        "```\n"
        "σ = √[∑(xᵢ - x̄)² / (n-1)]\n"
        "```\n\n"
        
        f"\n**Сумма квадратов:** `{sum_squared:.6f}`\n"
        f"**Деление на (n-1):** `{sum_squared:.6f} / {record_count-1} = {sum_squared/(record_count-1):.6f}`\n"
        f"**Извлечение корня:** `√{sum_squared/(record_count-1):.6f}`\n\n"
        
        "🎯 **Результат:**\n"
        f"```\n"
        f"σ = {result:.6f}\n"
        "```"
    )

def get_rmsm_message(record_count: int, s: float, result: float):
    return (
        "🎯 **Расчет СКО среднего значения**\n\n"
        
        "**Исходные данные:**\n"
        f"• Количество измерений: `{record_count}`\n"
        f"• Стандартное отклонение: `{s:.6f}`\n\n"
        
        "**Формула:**\n"
        "```\n"
        f"sₓ = σ / √n\n"
        f"   = {s:.6f} / √{record_count}\n"
        "```\n\n"
        
        "**Вычисления:**\n"
        f"• √{record_count} = `{sqrt(record_count):.6f}`\n"
        f"• {s:.6f} / {sqrt(record_count):.6f} = `{result:.6f}`\n\n"
        
        "📊 **Результат:**\n"
        f"```\n"
        f"sₓ = {result:.6f}\n"
        "```\n\n"
        "*СКО среднего показывает точность определения среднего значения*"
    )


def get_tpn_message(record_count: int, result: float) -> str:
    return (
        "📊 **Коэффициент Стьюдента**\n\n"
        
        "**Исходные данные:**\n"
        f"• Количество измерений: `{record_count}`\n"
        f"• Уровень доверия: `95%`\n"
        f"• Число степеней свободы: `{record_count - 1}`\n\n"
        
        "**Результат:**\n"
        f"```\n"
        f"t₍₀.₉₅, {record_count-1}₎ = {result}\n"
        "```\n\n"
        
    )

def get_error_rate_message(instrument_err_rate: float, tpn: float, s_: float ,result: float) -> str:
    return (
        "🔬 *Расчет полной погрешности*\n\n"
        
        "*Исходные данные:*\n"
        f"• Коэффициент Стьюдента (tₚ,ₙ): `{tpn:.4f}`\n"
        f"• СКО среднего (s): `{s_:.6f}`\n"
        f"• Приборная погрешность (Θ): `{instrument_err_rate:.6f}`\n\n"
        
        "*Формула:*\n"
        "```\n"
        "Δ = √[(tₚ,ₙ × s)² + Θ²]\n"
        "```\n\n"
        
        "*Вычисление:*\n"
        f"1. tₚ,ₙ × s = `{tpn:.4f} × {s_:.6f} = {tpn * s_:.6f}`\n"
        f"2. (tₚ,ₙ × s)² = `({tpn * s_:.6f})² = {(tpn * s_) ** 2:.8f}`\n"
        f"3. Θ² = `({instrument_err_rate:.6f})² = {instrument_err_rate ** 2:.8f}`\n"
        f"4. Сумма квадратов = `{(tpn * s_) ** 2:.8f} + {instrument_err_rate ** 2:.8f} = {((tpn * s_) ** 2) + (instrument_err_rate ** 2):.8f}`\n"
        f"5. √(суммы) = `√{((tpn * s_) ** 2) + (instrument_err_rate ** 2):.8f} = {result:.6f}`\n\n"
        
        f"📊 *Полная погрешность: Δ = {result:.6f}*"
    )


def get_result_message(value: float, erate: float, rounded_erate: float, rounded_value: float) -> str:
    return (
        "## 🎯 Оформление окончательного результата\n\n"
        
        "### Исходные данные:\n"
        f"- **Среднее значение**: `{value:.8f}`\n"
        f"- **Полная погрешность**: `{erate:.8f}`\n\n"
        
        "### Процесс округления:\n"
        f"1. **Анализ погрешности**: `{erate:.6f}`\n"
        f"2. **Первая значащая цифра**: `{rounded_erate}`\n"
        f"3. **Округленное среднее**: `{value:.6f}` → `{rounded_value}`\n"
        f"4. **Округленная погрешность**: `{erate:.6f}` → `{rounded_erate}`\n\n"
        
        "### 📊 Окончательный результат:\n"
        "```\n"
        f"x = ({rounded_value} ± {rounded_erate}) ед. изм.\n"
        "```\n\n"
        
    )
    