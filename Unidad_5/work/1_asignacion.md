# **Unidad 5:** Procesamiento por lotes - *Nube: Pipeline automatizado*

**NOTA:** En esta unidad implica trabajar con servicios en la nube que son cobrados por el proveedor de servicios en la nube. Consulte la [Calculadora de precios de AWS](https://calculator.aws/#/) para obtener una previsión del costo estimado de los servicios utilizados en este capítulo. Si continúan con esta unidad, lo hace bajo su responsabilidad, y el autor no tiene responsabilidad alguna por la factura resultante.

## Escenario
En el quinto sprint, necesita automatizar el pipeline que fue desarrollado en la nube de AWS a través de la consola. El pipeline debe ser implementable, actualizable y destructible bajo demanda de manera automatizada.

## Asignación
Para este Sprint, sus tareas incluyen:

1. **Leer** los siguientes temas en la sección [Teoría](#teoría):\
   a. Terraform.

2. **Implementar** los pasos en la sección [Práctica](#práctica) para la empresa *DataBookstone*:\
   a. Configurar servicios:
   - i. Crear usuario IAM.
   - ii. Crear clave de acceso.
   - iii. Configurar AWS CLI.
   - iv. Configurar Terraform.
   
   b. Ejecutar prueba de Terraform:
   - i. Preparar Terraform de prueba.
   - ii. Ejecutar Terraform init.
   - iii. Ejecutar Terraform plan.
   - iv. Ejecutar Terraform apply.
   - v. Ejecutar Terraform destroy.

   c. Desarrollar Terraform:
   - i. Preparar código de Terraform.
   - ii. Ejecutar Terraform init.
   - iii. Ejecutar Terraform plan.
   - iv. Ejecutar Terraform apply.
   - v. Verificar pipeline implementado.
   - vi. Ejecutar Terraform destroy.

3. **Completar** tareas para la empresa:
   - Revise la sección *Escenario*, complete los pasos en la *Asignación* y documente su trabajo en `work/1_asignacion.md`. Almacene toda la evidencia de su trabajo en el directorio `work`.

## Teoría
Las nociones teóricas principales del capítulo junto con recursos para aprendizaje autodirigido.

### Terraform

#### Descripción
HashiCorp Terraform es una herramienta de infraestructura como código que le permite definir recursos tanto en la nube como locales en archivos de configuración legibles para humanos que puede versionar, reutilizar y compartir. Luego puede usar un flujo de trabajo consistente para aprovisionar y gestionar toda su infraestructura a lo largo de su ciclo de vida. Terraform puede gestionar componentes de bajo nivel como recursos de computación, almacenamiento y red, así como componentes de alto nivel como entradas de DNS y características de SaaS.

#### Referencias
[HashiCorp - ¿Qué es Terraform?](https://developer.hashicorp.com/terraform/intro)\
[IBM - ¿Qué es Terraform?](https://www.ibm.com/topics/terraform)\
[GitHub - Terraform](https://github.com/hashicorp/terraform)

## Práctica
Implementación de la parte práctica del capítulo.

### Configurar servicios
Antes de proceder a automatizar la infraestructura, es necesario configurar algunas cosas como: crear un usuario IAM en AWS, instalar AWS CLI e instalar Terraform en su máquina local.

#### Crear usuario IAM
Inicie sesión en su cuenta de AWS con el usuario *root*. Navegue al servicio *IAM* y elija la opción `Usuarios`. Presione `Crear usuario` y proporcione un nombre para su usuario, se recomienda que sea `admin` ya que tendrá los mismos derechos o casi los mismos derechos que el usuario *root*. Marque la opción `Proporcionar acceso de usuario a la consola de administración de AWS` y elija `Deseo crear un usuario de IAM`. Para la *Contraseña de consola* elija cualquier contraseña, ya que será restablecida en el primer inicio de sesión, y presione `Siguiente`. En las `Opciones de permisos` elija `Adjuntar políticas directamente` y seleccione la política `AdministratorAccess`. Presione `Crear usuario`.\
Recibirá una URL para iniciar sesión en la consola, nombre de usuario y contraseña.

Usando la URL recibida, inicie sesión en su cuenta a través del usuario `admin` creado. Use el *ID de cuenta* de su cuenta.\
Se le pedirá que restablezca la contraseña. Ingrese la contraseña antigua que fue generada durante el proceso de creación del usuario o la contraseña que proporcionó en esa etapa.

Después de iniciar sesión con el usuario `admin`, verá que en lugar del nombre de su cuenta se especifica el usuario *admin*.

#### Generar clave de acceso
Navegue al servicio *IAM* y elija la sección *Usuarios*. Seleccione el usuario que fue creado anteriormente. En la sección *Resumen* presione la opción `Crear clave de acceso`. Para las *Mejores prácticas de claves de acceso y alternativas* elija la opción `Interfaz de línea de comandos`.

Se generará una clave de acceso y una clave de acceso secreta. Guarde estos valores ya que la clave de acceso secreta solo está disponible una vez y presione `Listo`.

Ahora puede ver que el usuario `admin` tiene una *Clave de acceso* activa y cuándo fue generada.

#### Configurar AWS CLI
Abra una terminal e ingrese el comando `aws --version` para verificar si *AWS CLI* está instalado en su máquina. Si aparece un mensaje *aws no se reconoce como un comando interno o externo*, siga la documentación para [Instalar o actualizar a la versión más reciente de AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

```
aws --version
```

Después de instalar *AWS CLI*, verifique una vez más la versión de *AWS CLI* en su máquina. Debería ver el mensaje *aws-cli n.nn.nn* que indica que la instalación fue exitosa.

Una vez que *AWS CLI* fue instalado, en la terminal ingrese el comando `aws configure` e ingrese la *ID de clave de acceso de AWS* que guardó anteriormente, la *Clave de acceso secreto de AWS* que guardó anteriormente, el *Nombre de región predeterminado* como `eu-central-1`, y el *Formato de salida predeterminado* como `json` y presione `Intro`.

```
aws configure
```

#### Configurar Terraform
Abra una terminal e ingrese el comando `terraform version` para verificar si *Terraform* está instalado en su máquina. Si aparece un mensaje *terraform no se reconoce como un comando interno o externo*, siga la documentación para [Instalar Terraform](https://developer.hashicorp.com/terraform/install?product_intent=terraform).

```
terraform version
```

Después de instalar *Terraform*, verifique una vez más la versión de *Terraform* en su máquina. Debería ver el mensaje *Terraform vn.nn.nn* que indica que la instalación fue exitosa.

### Ejecutar prueba de Terraform
Antes de comenzar a desarrollar código de infraestructura para el pipeline de *DrivenData*, se probará la configuración. Para la prueba de configuración se implementará un depósito S3 de prueba llamado `example-terraform-bucket-test`.

#### Preparar Terraform de prueba
Cree el directorio `test_terraform` y dentro cree un archivo `main.tf` y pegue el código siguiente.

```
provider "aws" {
  region = "eu-central-1"
}
```

En el mismo directorio cree un archivo `s3.tf` y copie el contenido siguiente.
El código para `main.tf` y `s3.tf` se puede encontrar en el directorio `src_5/test_terraform`.

```
resource "aws_s3_bucket" "s3_bucket" {
  bucket = "example-terraform-bucket-test"
}
```

#### Ejecutar Terraform init
En la terminal navegue al directorio `test_terraform` y ejecute el comando `terraform init`. Este comando inicializará terraform en este directorio y rastreará la infraestructura en este directorio.

```
terraform init
```

#### Ejecutar Terraform plan
En la terminal ejecute el comando `terraform plan`. Este comando preparará los recursos a implementar en la nube, verificará que no haya conflictos y mostrará qué recursos serán creados, actualizados o eliminados.

```
terraform plan
```

#### Ejecutar Terraform apply
En la terminal ejecute el comando `terraform apply`. Este comando aplicará todos los cambios en la infraestructura que fueron planeados en la etapa de plan y los recursos serán implementados en la nube. Debe escribir `yes` si está de acuerdo con todos los cambios que se realizarán y presione `Intro`.

```
terraform apply
```

Ahora puede navegar al servicio *S3* y verificar si el depósito fue implementado. Debería ver el depósito con el nombre `example-terraform-bucket-test`.

#### Ejecutar Terraform destroy
En la terminal ejecute el comando `terraform destroy`. Este comando destruirá todos los cambios en la infraestructura que fueron planeados en la etapa de plan y los recursos serán eliminados de la nube. Debe escribir `yes` si está de acuerdo con todos los cambios que se realizarán y presione `Intro`.

```
terraform destroy
```

### Desarrollar Terraform
Cree el directorio `terraform`. Todo el código de infraestructura del proyecto irá al directorio `terraform`. Los pasos principales serán los mismos que en el paso *Probar Terraform*, pero con todos los recursos involucrados en el pipeline desarrollado en el capítulo anterior.\
Todos los recursos se proporcionarán con la configuración mínima requerida y opciones.

#### Preparar código no-Terraform
En el directorio `terraform` cree subdirectorios: `dags` para archivos DAG, `policies` para políticas de IAM, `requirements` para dependencias, y `tasks` para archivos de trabajos de Glue.\
En el directorio `dags` copie el archivo DAG *driven_data_pipeline.py* del capítulo anterior.\
En el directorio `requirements` copie el archivo *requirements.txt* del capítulo anterior.\
En el directorio `tasks` copie los archivos de Python *dim_address.py*, *dim_date.py*, *dim_finance.py*, *dim_person.py* y *fact_network_usage.py* utilizados para trabajos de Glue del capítulo anterior.

#### Preparar código de Terraform
En el directorio `terraform` cree archivos llamados `main.tf` para la declaración del proveedor, un archivo `variables.tf` para la declaración de variables, un archivo `terraform.tfvars` para los valores de las variables, un archivo `glue.tf` para la implementación de base de datos, rastreadores y trabajos de Glue, un archivo `iam.tf` para la implementación de roles de IAM, un archivo `mwaa.tf` para la implementación de Airflow, un archivo `s3.tf` para la creación de depósito S3 y copia de archivos al depósito, y un archivo `vpc.tf` para la implementación de VPC, subredes y grupo de seguridad.\
En el subdirectorio `policies` cree un archivo `airflow_assume_role_policy.json.tpl` para la política de rol de Airflow, un archivo `airflow_execution_role_policy.json.tpl` para la política de rol de ejecución de Airflow, un archivo `glue_assume_role_policy.json.tpl` para la política de rol de Glue, y un archivo `glue_execution_role_policy.json.tpl` para la política de rol de ejecución de Glue.

**Declarar variables**\
En el archivo `variables.tf` pegue el contenido siguiente. Aquí definirá como variables, para una mejor gestión, todos los valores que se utilizan en el código de Terraform al menos dos veces. Se puede notar que algunas variables tienen un valor *default* y otras no. Aquellas variables que tienen un valor constante para todos los posibles entornos se declararán con valores predeterminados, aquellas variables que pueden cambiar el valor en función del entorno se almacenarán en el archivo `terraform.tfvars`.

```
variable "account_id" {
  description = "El ID de cuenta de AWS."
  type        = string
}

variable "region" {
  description = "La región del pipeline de DrivenData."
  type        = string
}

variable "tag" {
  description = "La etiqueta para el pipeline de DrivenData."
  default     = "driven_data"
}

variable "bucket_name" {
  description = "El nombre del depósito de S3."
  type        = string
  default     = "driven-data-bucket"
}

variable "mwaa_name" {
  description = "El nombre del entorno MWAA."
  type        = string
  default     = "driven-data-airflow-environment"
}

variable "personal_public_ip" {
  description = "Su dirección IP pública personal."
  type        = string
}
```

Para las variables que pueden cambiar el valor según el entorno, copie el contenido siguiente al archivo `terraform.tfvars`. Reemplace *ACCOUNT_ID* e *IP_PUBLICA* con sus valores.

```
account_id         = ACCOUNT_ID
region             = "eu-central-1"
personal_public_ip = IP_PUBLICA
```

**Definir el proveedor de Amazon Web Services**\
En el archivo `main.tf` pegue el contenido siguiente. El proveedor utilizado es *aws* y los recursos serán implementados en la región *eu-central-1*.

```
provider "aws" {
  region = var.region
}
```

**Definir depósito de Simple Storage Service**\
En el archivo `s3.tf` pegue el contenido siguiente. Esto implementará un depósito con configuraciones predeterminadas con nombre *driven-data-bucket*. El contenido completo del archivo se puede encontrar en `chapter_5/src_5/terraform/s3.tf`.

```
resource "aws_s3_bucket" "driven_data_bucket" {
  bucket = var.bucket_name
  tags = {
    Name = var.tag
  }
}
```

Para copiar los archivos DAG, requirements y tasks, use el bloque de código siguiente. Los recursos de copia para todo el contenido de los subdirectorios se pueden encontrar en el archivo `chapter_5/src_5/terraform/s3.tf`.

```
resource "aws_s3_object" "copy_dags" {
  for_each = fileset("dags/", "*")
  bucket   = aws_s3_bucket.driven_data_bucket.id
  key      = "dags/${each.value}"
  source   = "dags/${each.value}"
  etag     = filemd5("dags/${each.value}")
}
```

**Definir Nube Privada Virtual**\
En el archivo `vpc.tf` pegue el contenido siguiente. Esto implementará una VPC, dos subredes públicas y dos subredes privadas necesarias para MWAA, también implementará una puerta de enlace de Internet y asignará subredes a la puerta de enlace de Internet. Bloque de código para VPC.

```
resource "aws_vpc" "mwaa_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = var.tag
  }
}
```

Bloque de código para la subred. El código completo se encuentra en el archivo `chapter_5/src_5/terraform/vpc.tf`.

```
resource "aws_subnet" "public_subnet_1" {
  vpc_id            = aws_vpc.mwaa_vpc.id
  cidr_block        = "10.0.3.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = var.tag
  }
}
```

Bloque de código para la puerta de enlace de Internet.

```
resource "aws_internet_gateway" "mwaa_igw" {
  vpc_id = aws_vpc.mwaa_vpc.id
  tags = {
    Name = var.tag
  }
}
```

Bloque de código para el grupo de seguridad. Pegue el contenido siguiente. Esto implementará un grupo de seguridad utilizado para control de tráfico en Airflow. Permitirá tráfico entrante en un puerto específico y tráfico saliente para todos los puertos.

```
resource "aws_security_group" "mwaa_sg" {
  vpc_id = aws_vpc.mwaa_vpc.id
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.personal_public_ip]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = var.tag
  }
}
```

Bloque de código para la tabla de enrutamiento. Pegue el contenido siguiente. Esto implementará una tabla de enrutamiento y la asociará con la subred pública. El código completo se encuentra en el archivo `Unidad5/src/terraform/vpc.tf`.

```
resource "aws_route_table" "public_route_table" {
  vpc_id = aws_vpc.mwaa_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.mwaa_igw.id
  }
  tags = {
    Name = var.tag
  }
}

resource "aws_route_table_association" "public_subnet_1_assoc" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_route_table.id
}
```

**Definir Gestión de identidad y acceso**\
En el archivo `iam.tf` copie el contenido siguiente para crear la política y el usuario *Airflow*. Además, adjunte la política al usuario. El código completo se encuentra en el archivo `Unidad5/src/terraform/iam.tf`. También hay declaración del rol *Glue* utilizado para la ejecución de trabajos de Glue.

```
resource "aws_iam_role" "mwaa_execution_role" {
  name               = "mwaa_execution_role"
  description        = "Rol para la ejecución de MWAA."
  assume_role_policy = templatefile("${path.module}/policies/airflow_assume_role_policy.json.tpl", {})
  tags = {
    Name = var.tag
  }
}

resource "aws_iam_policy" "mwaa_policy" {
  name        = "mwaa_execution_policy"
  description = "Política para permisos de MWAA."

  policy = templatefile("${path.module}/policies/airflow_execution_role_policy.json.tpl", {
    region      = var.region
    account_id  = var.account_id
    bucket_name = var.bucket_name
    mwaa_name   = var.mwaa_name
  })
}

resource "aws_iam_role_policy_attachment" "mwaa_role_policy_attachment" {
  role       = aws_iam_role.mwaa_execution_role.name
  policy_arn = aws_iam_policy.mwaa_policy.arn
}
```

Para que la política *Airflow* sea utilizada por el rol *Airflow*, pegue el contenido siguiente al archivo `airflow_assume_role_policy.json.tpl`. Copie el contenido para todas las políticas desde el directorio `policies`.

```
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
            "Service": [
                "airflow.amazonaws.com",
                "airflow-env.amazonaws.com"
                ]
        },
        "Action": "sts:AssumeRole"
      }
   ]
}
```

**Definir Glue**\
En el archivo `glue.tf` defina la base de datos, rastreadores y trabajos de Glue a ser utilizados en el pipeline de *DrivenData*.\
Para la *base de datos* copie el contenido siguiente, implementará una base de datos que contendrá todos los datos del pipeline.

```
resource "aws_glue_catalog_database" "driven_data_db" {
  name = "driven_data_db"
  description = "Base de datos para datos de DrivenData."
  tags = {
    Name = var.tag
  }
}
```

Para el rastreador que actualizará datos sin procesar de S3 a la base de datos copie el contenido siguiente. El código completo se encuentra en el archivo `Unidad5/src/terraform/glue.tf`.

```
resource "aws_glue_crawler" "raw_driven_data_crawler" {
  name          = "raw_driven_data_crawler"
  role          = aws_iam_role.glue_execution_role.arn
  database_name = aws_glue_catalog_database.driven_data_db.name
  description   = "Rastreador que obtiene datos de S3 y crea tabla en la base de datos de Glue para datos sin procesar."
  s3_target {
    path = "${aws_s3_bucket.driven_data_bucket.bucket}/data/raw/"
  }
  tags = {
    Name = var.tag
  }
}
```

Para el trabajo de Glue que transformará y moverá datos de sin procesar a tabla de dirección de prueba, copie el contenido siguiente. El código completo se encuentra en el archivo `Unidad5/src/terraform/glue.tf`.

```
resource "aws_glue_job" "staging_dim_address_glue" {
  name        = "staging_dim_address_glue"
  description = "Trabajo de Glue para transformar datos de sin procesar a dirección de prueba."
  role_arn    = aws_iam_role.glue_execution_role.arn
  command {
    name            = "pythonshell"
    python_version  = "3.9"
    script_location = "s3://${aws_s3_bucket.driven_data_bucket.bucket}/tasks/dim_address.py"
  }
  tags = {
    Name = var.tag
  }
}
```

**Definir flujos de trabajo gestionados para Apache Airflow**\
En el archivo `mwaa.tf` defina el entorno de Airflow utilizado para orquestar el pipeline de *DrivenData*.

```
resource "aws_mwaa_environment" "mwaa_env" {
  name                 = var.mwaa_name
  airflow_version      = "2.9.2"
  execution_role_arn   = aws_iam_role.mwaa_execution_role.arn
  source_bucket_arn    = aws_s3_bucket.driven_data_bucket.arn
  max_workers          = 5
  min_workers          = 1
  environment_class    = "mw1.small"
  dag_s3_path          = "dags"
  requirements_s3_path = "requirements.txt"
  network_configuration {
    security_group_ids = [aws_security_group.mwaa_sg.id]
    subnet_ids         = [aws_subnet.private_subnet_1.id, aws_subnet.private_subnet_2.id]
  }
  logging_configuration {
    task_logs {
      enabled = true
      log_level = "INFO"
    }
    scheduler_logs {
      enabled = true
      log_level = "INFO"
    }
    webserver_logs {
      enabled = true
      log_level = "INFO"
    }
    worker_logs {
      enabled = true
      log_level = "INFO"
    }
    dag_processing_logs {
      enabled = true
      log_level = "INFO"
    }
  }
  webserver_access_mode = "PUBLIC_ONLY"
  tags = {
    Name = var.tag
  }
}
```

#### Ejecutar Terraform init
En la terminal navegue al directorio *terraform* e inicialice terraform en este directorio usando el comando siguiente.

```
terraform init
```

#### Ejecutar Terraform plan
Ejecute el comando siguiente para investigar si ocurrirá algún error durante la implementación y para analizar qué recursos serán implementados.

```
terraform plan
```

Después de ejecutar el comando anterior, terraform proporcionará un plan detallado con los recursos que serán implementados. Una instantánea de la declaración del comando *plan* se presenta siguiente. Puede ver que realizará los siguientes cambios: *42 a agregar, 0 a cambiar, 0 a destruir*.

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_iam_role_policy_attachment.mwaa_role_policy_attachment will be created
  + resource "aws_iam_role_policy_attachment" "mwaa_role_policy_attachment" {
      + id         = (known after apply)
      + policy_arn = (known after apply)
      + role       = "mwaa_execution_role"
    }

  # aws_iam_service_linked_role.airflow_linked_role will be created
  + resource "aws_iam_service_linked_role" "airflow_linked_role" {
      + arn              = (known after apply)
      + aws_service_name = "aws.amazonaws.com"
      + create_date      = (known after apply)
      + id               = (known after apply)
      + name             = (known after apply)
      + path             = (known after apply)
      + tags             = {
          + "Name" = "driven_data"
        }
      + tags_all         = {
          + "Name" = "driven_data"
        }
      + unique_id        = (known after apply)
    }

  # aws_internet_gateway.mwaa_igw will be created
  + resource "aws_internet_gateway" "mwaa_igw" {
      + arn      = (known after apply)
      + id       = (known after apply)
      + owner_id = (known after apply)
      + tags     = {
          + "Name" = "driven_data"
        }
      + tags_all = {
          + "Name" = "driven_data"
        }
      + vpc_id   = (known after apply)
      }

Plan: 42 to add, 0 to change, 0 to destroy.
```

#### Ejecutar Terraform apply
Ejecute el comando siguiente para aplicar los cambios que se presentaron en *plan*. Después de ejecutar el comando, ingrese `yes` si está de acuerdo con los cambios que se aplicarán a la infraestructura de nube.

```
terraform apply
```

A continuación se presenta una instantánea del proceso de aplicación de terraform. Tomará aproximadamente 1 hora implementar todos los recursos para el pipeline de *DrivenData*.

```
aws_glue_catalog_database.staging_dim_address_db: Creating...
aws_vpc.mwaa_vpc: Creating...
aws_glue_catalog_database.staging_dim_date_db: Creating...
aws_glue_catalog_database.staging_dim_finance_db: Creating...
aws_glue_catalog_database.staging_dim_person_db: Creating...
aws_glue_catalog_database.staging_fact_network_usage_db: Creating...
aws_iam_role.glue_execution_role: Creating...
aws_glue_catalog_database.raw_driven_data_db: Creating...
aws_iam_role.mwaa_execution_role: Creating...
aws_s3_bucket.driven_data_bucket: Creating...
```

#### Verificar pipeline implementado
Después de que la implementación se haya completado y todos los recursos estén disponibles, se puede ejecutar el pipeline.\
Navegue a *MWAA* y verá el *driven-data-airflow-environment* disponible.

En cada recurso que fue implementado se puede ver la etiqueta *driven_data* disponible. Etiquetar los recursos basados en diferentes claves es muy importante para la gestión de recursos.

En el depósito de S3 están presentes los directorios creados inicialmente: *dags* y *tasks* que contienen todos los archivos específicos, así como el archivo *requirements.txt*.

Los cinco trabajos de Glue que se utilizan en el pipeline se implementan y están disponibles.

Todos los seis rastreadores que se utilizan en el pipeline se implementan y están disponibles.

La base de datos también se implementa y está disponible para ser utilizada para el pipeline de *DrivenData*.

Los roles que fueron declarados se implementan y están disponibles para ejecutar trabajos específicos para los que fueron asignados.

#### Ejecutar Terraform destroy
Después de que el trabajo esté completo y los recursos ya no sean necesarios, destruya todos los recursos implementados usando el comando siguiente.

```
terraform destroy
```

**Nota:** La computación en la nube no es gratuita. Implementar recursos algunas veces y ejecutar el pipeline durante dos días cuesta aproximadamente 30 USD. No utilice servicios facturables si no desea ser cobrado por usar los servicios de AWS.
