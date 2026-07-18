// https://platform.openai.com/docs/guides/function-calling

const tools = [{
    type: "function",
    name: "update_citizen_score",
    description: "Update the loyalty score of a citizen.",
    parameters: {
        type: "object",
        properties: {
            citizen_id: { type: "number", description: "numeric #id of the citizen" },
            score: { type: "number", description: "citizen score between 0 and 100" }
        },
        required: ["citizen_id", "score"],
        additionalProperties: false
    },
    strict: true
}];