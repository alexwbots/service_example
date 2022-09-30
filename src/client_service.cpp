#include "ros/ros.h"
#include "service_example/Archivo_var.h"
#include <cstdlib>

int main(int argc, char **argv) {

  ros::init(argc, argv, "service_client");
  ros::NodeHandle n;
  ros::ServiceClient client = n.serviceClient<service_example::Archivo_var>("filtro");
  service_example::Archivo_var srv;

  std::vector<float> a;

  a.push_back(23.2);
  a.push_back(22.1);

  srv.request.valores = a;
  if (client.call(srv))
  {
    ROS_INFO("Resultado del filtrado: %f", (float)srv.response.resultado);
  } 
  else {
    ROS_ERROR("Fallo el llamado al servicio del filtrado");
    return 1;
  }
  return 0;
}
