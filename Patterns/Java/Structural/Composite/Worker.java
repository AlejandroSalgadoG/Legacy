public abstract class Worker{

    protected String name;

    public Worker(String name){
        this.name = name;
    }

    abstract public void add(Worker worker);
    abstract public void remove(Worker worker);
    abstract public void displayStructure();
}
