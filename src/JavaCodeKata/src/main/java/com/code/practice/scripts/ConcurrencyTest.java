package com.code.practice.scripts;

import com.code.practice.infra.Script;
import com.code.practice.infra.ScriptInterface;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import org.springframework.stereotype.Component;

@Component
public class ConcurrencyTest extends Script implements ScriptInterface {

    public ConcurrencyTest() {
        setDescription("Script to test java concurrency with locks and mutexes");
        setScriptName("concurrency");
    }

    public boolean run(String... args) {

        return false;
    }
}
