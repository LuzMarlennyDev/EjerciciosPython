print ("Seleccione el producto que desea comprar");
print("1. tinto" );
print("2. cafe" );
print("3. capuccino" );
print("4. te verde" );
producto=int(input());
if producto ==1:
    print("Usted ha seleccionado tinto");
    precio=1500;
    print("Digite la cantidad que desea comprar");
    cantidad=int(input());
    total=precio*cantidad;
    print("El total a pagar es:",total); 
    if cantidad>=10 and cantidad<20:
        descuento=total*0.05;
        print("Usted tiene un descuento del 5% por comprar 10 a 19 unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);

    if cantidad>=20 and cantidad<30:
        descuento=total*0.1;
        print("Usted tiene un descuento del 10% por comprar 20 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);
    if cantidad<10:
        print("No tiene descuento");
        print("El total a pagar es:",total);
    if cantidad>30:
        descuento=total*0.15;
        print("Usted tiene un descuento del 15% por comprar 0 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total); 
if producto ==2:
    print("Usted ha seleccionado cafe");
    precio=2000;
    print("Digite la cantidad que desea comprar");
    cantidad=int(input());
    total=precio*cantidad;
    print("El total a pagar es:",total);
    if cantidad>=10 and cantidad<20:
        descuento=total*0.05;
        print("Usted tiene un descuento del 5% por comprar 10 a 19 unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
    print("El total a pagar con el descuento es:",total);
if producto ==3:
    print("Usted ha seleccionado Capuchino");
    precio=1500;
    print("Digite la cantidad que desea comprar");
    cantidad=int(input());
    total=precio*cantidad;
    print("El total a pagar es:",total); 
    if cantidad>=10 and cantidad<20:
        descuento=total*0.05;
        print("Usted tiene un descuento del 5% por comprar 10 a 19 unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);

    if cantidad>=20 and cantidad<30:
        descuento=total*0.1;
        print("Usted tiene un descuento del 10% por comprar 20 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);
    if cantidad<10:
        print("No tiene descuento");
        print("El total a pagar es:",total);
    if cantidad>30:
        descuento=total*0.15;
        print("Usted tiene un descuento del 15% por comprar 0 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total); 
if producto ==4:
    print("Usted ha seleccionado Te verde");
    precio=1500;
    print("Digite la cantidad que desea comprar");
    cantidad=int(input());
    total=precio*cantidad;
    print("El total a pagar es:",total); 
    if cantidad>=10 and cantidad<20:
        descuento=total*0.05;
        print("Usted tiene un descuento del 5% por comprar 10 a 19 unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);

    if cantidad>=20 and cantidad<30:
        descuento=total*0.1;
        print("Usted tiene un descuento del 10% por comprar 20 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total);
    if cantidad<10:
        print("No tiene descuento");
        print("El total a pagar es:",total);
    if cantidad>30:
        descuento=total*0.15;
        print("Usted tiene un descuento del 15% por comprar 0 o mas unidades");
        print("El valor del descuento es:",descuento);
        total=total-descuento;
        print("El total a pagar con el descuento es:",total); 