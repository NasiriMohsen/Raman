#MACHINE LIBRARY
import machine

#SET GPIO OUTPUT/INPUT (0,2,4,5,12,13,14,15,16)
#OUTPUT
pin = machine.Pin(0)
pin = machine.Pin(0, machine.Pin.OUT)
#INPUT
pin = machine.Pin(0, machine.Pin.IN)
pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#OUTPUT 0/1
pin.value(0)
pin.value(1)
pin.off()
pin.on()

#INPUT READ VAL
pin.value()

#INTERUPT
pin.irq(trigger=Pin.IRQ_FALLING, handler=Function)
pin.irq(trigger=Pin.IRQ_RISING, handler=Function)
pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=Function)

#MAKE PIN PWM
Ppin = machine.PWM(pin)
Ppin = machine.PWM(machine.Pin(2), freq=500, duty=512)

#SET PWM FREQ AND CYCLE
Ppin.freq(500)
Ppin.duty(512)

#SHOW PWM VALUES
Ppin.freq()
Ppin.duty()
print(Ppin)

#DISMISS PWM
Ppin.deinit()

#SET PWM FREQ AND CYCLE FOR "SERVO"
Ppin.freq(50)
#MIN
Ppin.duty(40)
#MID
Ppin.duty(77)
#MAX
Ppin.duty(115)

#SET PWM FREQ AND CYCLE FOR "LED"
Ppin.freq(1000)
#MIN
Ppin.duty(0)
#MID
Ppin.duty(512)
#MAX
Ppin.duty(1024)

#ANALOG PIN
adc = machine.ADC(0)

#ANALOG READ
adc.read()

#CPU FREQ SHOW DEFAULT IS 80MHz
print(machine.freq())

#CPU CHANGE FREQ AT THE COST OF CURENT TO 160MHz
machine.freq(160000000)


