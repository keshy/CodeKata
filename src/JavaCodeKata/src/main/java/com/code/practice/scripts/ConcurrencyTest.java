package com.code.practice.scripts;

import com.code.practice.infra.Script;
import com.code.practice.infra.ScriptInterface;
import org.springframework.stereotype.Component;

import java.util.Stack;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

@Component
public class ConcurrencyTest extends Script implements ScriptInterface {

    private static Stack<String> hydrogenStack = new Stack<String>();
    private static Stack<String> oxygenStack = new Stack<String>();
    private Lock lock = new ReentrantLock();
    private boolean water = false;
    private boolean acquired = false;
    private static int count = 0;

    public ConcurrencyTest() {
        setDescription("Script to test java concurrency with locks and mutexes");
        setScriptName("concurrency");
    }

    public String hydrogen() throws InterruptedException {
        log.info("Received request for water with a hydrogen atom. Current state of water: " + water);
        hydrogenStack.add("H");
        while(!water) {
            try {

                acquired = lock.tryLock(TimeUnit.SECONDS.toSeconds(1), TimeUnit.SECONDS);
                if(acquired) {
                    log.info("Received exclusive re-entrant lock for hydrogen");
                    if (hydrogenStack.size() >= 2 && oxygenStack.size() >= 1) {
                        hydrogenStack.pop();
                        hydrogenStack.pop();
                        oxygenStack.pop();
                        water = true;
                        count = 3;
                    } else if (count > 0) {
                        water = true;
                        log.info("Servicing pending h2 requests - count:" + count);
                        count--;
                    } else {
                        water = false;
                    }
                }
            } catch (InterruptedException e) {
                log.severe("thread interrupted exception: " + e);
            } finally {
                if(acquired) {
                    lock.unlock();
                }
            }
            Thread.sleep(2000L);
        }

        return "H20";

    }

    public String oxygen() throws InterruptedException {
        log.info("Received request for water with a oxygen atom. Current state of water: " + water);
        oxygenStack.add("O");
        while(!water) {
            try {

                acquired = lock.tryLock(TimeUnit.SECONDS.toSeconds(1), TimeUnit.SECONDS);
                if(acquired) {
                    log.info("Received exclusive re-entrant lock for oxygen");
                    if (hydrogenStack.size() >= 2 && oxygenStack.size() >= 1) {
                        hydrogenStack.pop();
                        hydrogenStack.pop();
                        oxygenStack.pop();
                        water = true;
                        count = 3;
                    } else if (count > 0) {
                        water = true;
                        log.info("Servicing pending o2 requests : count " + count);
                        count--;
                    } else {
                        water = false;
                    }
                }
            } catch (InterruptedException e) {
                log.severe("thread interrupted exception: " + e);
            } finally {
                if(acquired) {
                    lock.unlock();
                }
            }
            Thread.sleep(2000L);
        }

        return "H20";

    }
    public boolean run(String... args) {
        Thread t1 = new Thread(new Runnable() {
            public void run() {
                ConcurrencyTest t = new ConcurrencyTest();
                try {
                    log.info("Received: " + t.hydrogen() + " t1 complete");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t2 = new Thread(new Runnable() {
            public void run() {
                ConcurrencyTest t = new ConcurrencyTest();
                try {
                    log.info("Received: " + t.hydrogen() + " t2 complete");

                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t3 = new Thread(new Runnable() {
            public void run() {
                ConcurrencyTest t = new ConcurrencyTest();
                try {
                    log.info("Received: " + t.oxygen() + " t3 complete");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t4 = new Thread(new Runnable() {
            public void run() {
                ConcurrencyTest t = new ConcurrencyTest();
                try {
                    log.info("Received: " + t.oxygen() + " t4 complete");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        Thread t5 = new Thread(new Runnable() {
            public void run() {
                ConcurrencyTest t = new ConcurrencyTest();
                try {
                    log.info("Received: " + t.hydrogen() + " t5 complete");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });

        try {
            Thread.sleep(2000L);
            t1.start();
            t2.start();
            t3.start();
            t4.start();
            t5.start();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return true;
    }
}
