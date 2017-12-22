package net.maurerit.microservices;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.stereotype.Controller;

@SpringBootApplication
@Controller
@EnableZuulProxy
public class GatewayServer {
    
    public static void main(String[] args) {
        new SpringApplicationBuilder(GatewayServer.class).web(true).run(args);
    }
}
