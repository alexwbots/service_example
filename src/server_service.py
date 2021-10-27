#!/usr/bin/env python
import rospy
from service_example.srv import Archivo_var, Archivo_varResponse

def funcion(request): # funcion tipo callback

  filtro = request.valores[1]*0.0609 + request.valores[0]*0.9391
  rospy.loginfo("Resultado del filtrado: "+str(filtro))
  return Archivo_varResponse(filtro) 

if __name__ == "__main__":

  rospy.init_node('service_server')
  server = rospy.Service('filtro', Archivo_var, funcion)
  rospy.loginfo("Filtro servidor esta listo!")
  rospy.spin()

# Archivo_var.srv
# float32[] valores
# ---
# float32 resultado