#include "ros/ros.h"
#include "service_example/Archivo_var.h"

bool filtro_funcion(service_example::Archivo_var::Request &req, service_example::Archivo_var::Response &res)
{
  res.resultado = req.valores[1] * 0.9391 + req.valores[0] * 0.0609;
  ROS_INFO("Resultado del filtrado: [%f]", res.resultado);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "service_server");
  ros::NodeHandle n;
  ros::ServiceServer service = n.advertiseService("filtro", filtro_funcion);
  ROS_INFO("Filtro servidor esta listo!");
  ros::spin();

  return 0;
}