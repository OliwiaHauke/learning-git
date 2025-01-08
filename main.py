print("Lista zakupów pętla")
shopping_items = [
    ("roquefort", 12.50),
    ("stilton", 11.24),
    ("brie", 9.30),
    ("gouda", 8.55),
    ("edam", 11.00),
    ("parmezan", 16.50),
    ("mozzarella", 14.00),
    ("czechosłowacki ser z owczego mleka", 122.32)
]
for name, price in shopping_items:
  shopping_list = f"Ser {name}: cena {price:.2f} zł/kg"
  print(shopping_list)
print("koteczki")
