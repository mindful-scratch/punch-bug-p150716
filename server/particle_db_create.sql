
DROP TABLE hinoqi_particle.power;

CREATE TABLE hinoqi_particle.power(
	id INT AUTO_INCREMENT UNIQUE, 
	dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	val INT, 
	done BOOLEAN DEFAULT FALSE);

CREATE INDEX datetime_index ON hinoqi_particle.power(dt);



