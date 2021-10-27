#!/usr/bin/env python
#import rospy
#from Nombre_Paquete.srv import Archivo_Variables, Archivo_VariablesResponse

#def funcion(request): # funcion tipo callback
#  variable = request.varible_entrada
#  # ... Codigo ...
#  return Archivo_VariablesResponse(resultado) 

#if __name__ == "__main__":

#  rospy.init_node('nombre_nodo')
#  server = rospy.Service('nombre_servicio', Archivo_Variables, funcion)
#  # o
#  # rospy.Service('nombre_servicio', Archivo_Variables, funcion)
#  rospy.spin()

################# Archivo SRV #################

# Archivo_Variables.srv
# Tipo_msgs variable_entrada
# ---
# Tipo_msgs variable_salida
