import offequip
import warehouse

pr1 = offequip.Printer('HP', 'DeskJet', 2500.5)
print(pr1)
print(f'Проверим работу принтера:\n{"-" * 36}')
print(pr1.turning_on())
print(pr1.printing())
print(pr1.turning_off())

storage = warehouse.OffEquipWarehouse()

print(f'Передаём технику на склад:\n{"-" * 36}')
storage.take_for_storage(pr1)

sca1 = offequip.Scanner('Cannon', 'Canoscan', 1300.5)
print(sca1)
print(f'Проверим работу сканера:\n{"-" * 36}')
print(sca1.turning_on())
print(sca1.scanning())
print(sca1.turning_off())

print(f'Передаём технику на склад:\n{"-" * 36}')
storage.take_for_storage(sca1)

cop1 = offequip.Copier('Cannon', 'imageRUNNER', 7000.5)
print(cop1)
print(f'Проверим работу копира:\n{"-" * 36}')
print(cop1.turning_on())
print(cop1.copying())
print(cop1.turning_off())

print(f'Передаём технику на склад:\n{"-" * 36}')
storage.take_for_storage(cop1)

mfd1 = offequip.MultiDevice('Brother', 'DCP', 5500.3)
print(mfd1)
print(f'Проверим работу МФУ:\n{"-" * 36}')
print(mfd1.turning_on())
print(mfd1.printing())
print(mfd1.scanning())
print(mfd1.copying())
print(mfd1.turning_off())

print(f'Передаём технику на склад:\n{"-" * 36}')
storage.take_for_storage(mfd1)

print(f'Проверим склад:\n{"-" * 36}')
print(storage)
print(storage.accounting())

storage.transfer_equipment(sca1)
print(f'Передадим требуемую оргтехнику заказчику:\n{"-" * 36}')
print(f'Проверим склад:\n{"-" * 36}')
print(storage)
print(storage.accounting())

print(f'Добавим ещё пару единиц оргтехники:\n{"-" * 36}')
mfd2 = offequip.MultiDevice('Samsung', 'Multiscan - 100500', 15500.3)
sca2 = offequip.Scanner('Cannon', 'Canoscan', 1300.5)
storage.take_for_storage(mfd2)
storage.take_for_storage(sca2)

print(f'Проверим склад:\n{"-" * 36}')
print(storage)
print(storage.accounting())

print(f'Попробуем добавить на склад "Васю Пупкина":\n{"-" * 36}')
abc = 'Вася Пупкин'
storage.take_for_storage(abc)

pr2 = offequip.Printer('HP', 'DeskJet', '2500.5')
