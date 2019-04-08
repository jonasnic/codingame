import java.util.*;

class Player {
  public static void main(String args[]) {
    Skynet skynet = new Skynet();
    skynet.readInitInput();
    skynet.gameLoop();
  }
}

class Moto {
  int x; // x coordinate of the motorbike
  int y; // y coordinate of the motorbike
  boolean active; // indicates whether the motorbike is activated

  Moto(int x, int y, boolean active) {
    this.x = x;
    this.y = y;
    this.active = active;
  }

  Moto(Moto moto) {
    x = moto.x;
    y = moto.y;
    active = moto.active;
  }
}

class State {
  int hSpeed; // the motorbikes' horizontal speed
  List<Moto> motos = new ArrayList<>();

  State(int hSpeed) {
    this.hSpeed = hSpeed;
  }

  State(State state) {
    hSpeed = state.hSpeed;
    for (Moto moto : state.motos) {
      add(new Moto(moto));
    }
  }

  boolean add(Moto moto) {
    return motos.add(moto);
  }

  int nbActive() {
    int total = 0;
    for (Moto moto : motos) {
      if (moto.active) {
        total += 1;
      }
    }
    return total;
  }
}

class Skynet {
  Scanner in = new Scanner(System.in);
  int nbMotos; // the amount of motorbikes to control
  int minSurvivors; // the minimum amount of motorbikes that must survive
  String lanes[]; // lanes of the road

  Action speed = new Speed();
  Action up = new Up();
  Action down = new Down();
  Action jump = new Jump();
  Action slow = new Slow();
  Action[] actions = {speed, up, down, jump, slow};

  void readInitInput() {
    nbMotos = in.nextInt();
    minSurvivors = in.nextInt();
    String lane0 = in.next();
    String lane1 = in.next();
    String lane2 = in.next();
    String lane3 = in.next();
    lanes = new String[]{lane0, lane1, lane2, lane3};
  }

  void gameLoop() {
    while (true) {
      int speed = in.nextInt(); // the motorbikes' hSpeed
      State initialState = new State(speed);
      for (int i = 0; i < nbMotos; i++) {
        int x = in.nextInt();
        int y = in.nextInt();
        boolean active = in.nextInt() == 1;
        Moto moto = new Moto(x, y, active);
        initialState.add(moto);
      }

      Action action = null;
      if (nbMotos == 4)
        action = play(initialState, nbMotos, 1); // for achievement
      if (action == null)
        action = play(initialState, minSurvivors, 1);
      System.out.println(action);
    }
  }

  // recursive solution
  Action play(State currentState, int nbSurvivors, int nbTurns) {
    // check recursion depth
    if (nbTurns > 10) {
      return speed;
    }

    // end of the bridge?
    if (currentState.motos.get(0).x > lanes[0].length() - 1) {
      return slow;
    }

    // compute all possible actions
    for (Action action : actions) {
      if (isValid(action, currentState)) {
        State nextState = action.apply(currentState);
        if (nextState.nbActive() >= nbSurvivors) {
          Action nextAction = play(nextState, nbSurvivors, nbTurns + 1);
          if (nextAction != null) {
            return action;
          }
        }
      }
    }

    return null;
  }

  // validate UP and DOWN actions
  boolean isValid(Action action, State currentState) {
    if (action == up || action == down) {
      if (currentState.nbActive() == 4) {
        return false;
      }

      for (Moto moto : currentState.motos) {
        if (action == up && moto.y == 0) {
          return false;
        } else if (action == down && moto.y == 3) {
          return false;
        }
      }
    }
    return true;
  }

  void move(Moto moto, int hSpeed, int vSpeed, boolean jump) {
    final char HOLE = '0';

    // last cell straight ahead
    int x = moto.x + hSpeed;
    if (vSpeed == 0 && x < lanes[0].length() && lanes[moto.y].charAt(x) == HOLE) {
      moto.active = false;
      return;
    }

    if (!jump) {
      // straight ahead
      for (x = moto.x + 1; x < Math.min(moto.x + hSpeed, lanes[0].length()); ++x) {
        if (lanes[moto.y].charAt(x) == HOLE) {
          moto.active = false;
          return;
        }
      }

      // UP or DOWN
      if (vSpeed != 0) {
        int y = moto.y + vSpeed;
        for (x = moto.x + 1; x <= moto.x + hSpeed && x < lanes[0].length(); ++x) {
          if (lanes[y].charAt(x) == HOLE) {
            moto.active = false;
            return;
          }
        }
      }
    }
    moto.x += hSpeed;
    moto.y += vSpeed;
  }

  interface Action {
    State apply(State state);
  }

  class Speed implements Action {
    @Override
    public State apply(State state) {
      State nextState = new State(state);
      nextState.hSpeed += 1;

      for (Moto moto : nextState.motos) {
        if (moto.active) {
          move(moto, nextState.hSpeed, 0, false);
        }
      }

      return nextState;
    }

    @Override
    public String toString() {
      return "SPEED";
    }
  }

  class Up implements Action {
    @Override
    public State apply(State state) {
      State nextState = new State(state);

      for (Moto moto : nextState.motos) {
        if (moto.active) {
          move(moto, nextState.hSpeed, -1, false);
        }
      }

      return nextState;
    }

    @Override
    public String toString() {
      return "UP";
    }
  }

  class Down implements Action {
    @Override
    public State apply(State state) {
      State nextState = new State(state);

      for (Moto moto : nextState.motos) {
        if (moto.active) {
          move(moto, nextState.hSpeed, 1, false);
        }
      }

      return nextState;
    }

    @Override
    public String toString() {
      return "DOWN";
    }
  }

  class Jump implements Action {
    @Override
    public State apply(State state) {
      State nextState = new State(state);

      for (Moto moto : nextState.motos) {
        if (moto.active) {
          move(moto, nextState.hSpeed, 0, true);
        }
      }

      return nextState;
    }

    @Override
    public String toString() {
      return "JUMP";
    }
  }

  class Slow implements Action {
    @Override
    public State apply(State state) {
      State nextState = new State(state);
      nextState.hSpeed -= 1;

      for (Moto moto : nextState.motos) {
        if (moto.active) {
          move(moto, nextState.hSpeed, 0, false);
        }
      }

      return nextState;
    }

    @Override
    public String toString() {
      return "SLOW";
    }
  }
}
