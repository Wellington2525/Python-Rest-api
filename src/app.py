from ast import Try
#from crypt import methods
from urllib import response
from flask import Flask
from flask_mysqldb import MySQL
from config import config
import pymysql
from flask import jsonify
from flask import flash, request


app = Flask(__name__)

conexion=MySQL(app)

@app.route('/emp')
def listar_emp():
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("""SELECT * FROM tblempleados""")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        print(response)
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        #conn.close()    

#########Leer/id###############
@app.route('/leer_id/<codigo>', methods=['GET'])
def leer_id(codigo):
    try:
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT id,nombre,apellido,cedula,direccion,telefono FROM tblempleados where id ='{0}'".format(codigo))
        datos = cursor.fetchone()
        if datos != None:
             response = {'id':datos[0],'nombre':datos[1],'apellido':datos[2],'cedula':datos[3],'direccion':datos[4],'telefono':datos[5]}
             return response
        else:
             return jsonify({'Mensaje': "Empleado no encontrado"})
        # respone = jsonify(empRows)
        # respone.status_code = 200
        
       
        # return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        #conn.close() 
   
#########Insert###############
@app.route('/create',methods=['POST'])
def create_emp():
     #sqlQuery = "INSERT INTO tblempleados(nombre,apellido,cedula,direccion,telefono) VALUES(%s,%s,%s,%s,%s)"
      #bindData =(_nombre,_apellido,_cedula,_direccion,_telefono)
    try:   
        cursor = conexion.connection.cursor()
        sqlQuery = """INSERT INTO tblempleados(nombre,apellido,cedula,direccion,telefono) VALUES('{0}','{1}','{2}','{3}','{4}')""".format(request.json['nombre'],request.json['apellido'],request.json['cedula'],request.json['direccion'],request.json['telefono'])
        cursor.execute(sqlQuery)
        conexion.connection.commit()
        return jsonify({'Mensaje':'Empleado registrado'})
           
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        #conn.close()

#########Update###############
@app.route('/edit/<codigo>',methods=['PUT'])
def edit_emp(codigo):
     #sqlQuery = "INSERT INTO tblempleados(nombre,apellido,cedula,direccion,telefono) VALUES(%s,%s,%s,%s,%s)"
      #bindData =(_nombre,_apellido,_cedula,_direccion,_telefono)
    try:   
        cursor = conexion.connection.cursor()
        sqlQuery = """UPDATE tblempleados SET nombre='{0}',apellido='{1}',cedula='{2}',direccion='{3}',telefono='{4}' where id={5} """.format(request.json['nombre'],request.json['apellido'],request.json['cedula'],request.json['direccion'],request.json['telefono'],codigo)
        cursor.execute(sqlQuery)
        conexion.connection.commit()
        return jsonify({'Mensaje':'Empleado actualizado'})
           
    except Exception as e:
        print(e)
    finally:
        cursor.close()

#########Delete###############
@app.route('/eliminar/<codigo>',methods=['DELETE'])
def eliminar(codigo):
     #sqlQuery = "INSERT INTO tblempleados(nombre,apellido,cedula,direccion,telefono) VALUES(%s,%s,%s,%s,%s)"
      #bindData =(_nombre,_apellido,_cedula,_direccion,_telefono)
    try:   
        cursor = conexion.connection.cursor()
        sqlQuery = "DELETE FROM tblempleados WHERE id= '{0}'".format(codigo)
        cursor.execute(sqlQuery)
        conexion.connection.commit()
        return jsonify({'Mensaje':'Empleado eliminado'})
           
    except Exception as e:
        print(e)
    finally:
        cursor.close()





if __name__== '__main__':
    app.config.from_object(config['development'])
    app.run()
  