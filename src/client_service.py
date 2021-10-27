#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64MultiArray
from service_example.srv import Archivo_var

valor_anterior = 0

if __name__ == "__main__":

  rospy.init_node('service_client')
  rospy.wait_for_service('filtro')
  client = rospy.ServiceProxy('filtro', Archivo_var)

  array = [23.2,22.1]
  variable = client(array)
  resultado = variable.resultado
  print("Resultado del filtro: "+str(resultado))

# Archivo_var.srv
# float32[] valores
# ---
# float32 resultado
