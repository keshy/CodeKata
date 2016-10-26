package com.code.practice.infra;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.ComponentScan;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Logger;

@EnableAutoConfiguration
@ComponentScan(basePackages = {"com.code.practice.scripts"})
@SpringBootApplication
public class ScriptRunner implements CommandLineRunner {

    public Logger log = Logger.getLogger("Scripts");

    @Autowired
    ApplicationContext context;

    @Autowired
    List<ScriptInterface> scripts;

    /**
     * Method to find the right script based on arguments provided
     *
     * @param className The case insensitive script name
     * @return the interface implementation for the matched script if available otherwise null
     */
    private ScriptInterface findScript(String className) {
        for (ScriptInterface script : scripts) {
            if (script.getClass().getSimpleName().equalsIgnoreCase(className)) {
                return script;
            }
        }
        return null;
    }

    public void run(String... strings) throws Exception {
        if (strings == null || strings.length < 1) {
            log.severe("No script name entered..");
            List<String> scriptNames = new ArrayList<String>();
            // dump all scripts found so far.
            for(ScriptInterface script: scripts) {
                scriptNames.add(script.getClass().getSimpleName());
            }
            log.info("\n============================Script name must match one of the following=========================" +
                    "\n" + scriptNames);
        } else {
            ScriptInterface script = findScript(strings[0]);
            if (script != null) {
                script.run(Arrays.asList(strings).subList(1, strings.length).toArray(new String[strings.length - 1]));
            } else {
                log.severe("Cannot find script: " + strings[0]);
            }
        }

        ((ConfigurableApplicationContext) context).close();
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(ScriptRunner.class, args);
    }
}
