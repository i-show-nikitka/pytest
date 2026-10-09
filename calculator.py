def calculate_commission(amount: int) ->  float:
  """
  Расчитывает комиссию денежного перевода
  
  Args:
      amount (int): Сумма перевода (от 100 до 50 000 рублей)
      
  
  Returns:
      float: Размер комиссии
      
  Raises:
      ValueError: Если сумма не входит в допустимый диапазон
      TypeError: Если тип данных на входе не int
  """
  
  if not isinstance(amount, int):
    raise TypeError("Неверный тип данных")
  if amount < 100  or amount > 50000:
    raise ValueError("Сумма перевода должна быть от 100 до 50 000 руб.")
  if amount <= 1000:
    return 50.0
  elif amount <= 20000:
    return 100.0
  elif amount <= 40000:
    return 200.0 + (amount * 0.01)
  else:
    return 500.0

  
  
  
  
