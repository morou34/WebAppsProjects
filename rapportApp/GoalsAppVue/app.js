Vue.createApp({
  data() {
    return {
      goals: [],
      goalInput: "",
    };
  },
  methods: {
    addGoal() {
      if (this.goalInput !== "") {
        this.goals.push(this.goalInput);
        this.goalInput = "";
      }
    },
    anotherMethod() {},
  },
  removeGoals() {
    this.goals = [];
  },
}).mount("#app");
