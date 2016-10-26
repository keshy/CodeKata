package com.code.practice.infra;

import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.internal.HelpScreenException;

import java.util.logging.Logger;

public class Script {

    public Logger log = Logger.getLogger("Scripts");

    private String description;
    private String scriptName;

    public ArgumentParser parser;


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getScriptName() {
        return scriptName;
    }

    public void setScriptName(String scriptName) {
        this.scriptName = scriptName;
    }

    public ArgumentParser getParser() {
        parser = ArgumentParsers.newArgumentParser(getScriptName())
                .defaultHelp(true)
                .description(getDescription());
        return parser;
    }

    public Namespace parseArgs(String... args) {
        try {
            return parser.parseArgs(args);
        } catch (HelpScreenException e) {
            System.exit(0);
        }
        catch (ArgumentParserException e) {
            log.severe("Error parsing arguments to script." + e);
            parser.handleError(e);
            System.exit(1);
        }
        return null;
    }
}
