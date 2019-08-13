package com.moodopa.pricone;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan(basePackages = "com.moodopa.pricone")
public class PriconeApplication {

	public static void main( String[] args ) {
		SpringApplication.run( PriconeApplication.class, args );
	}
}
