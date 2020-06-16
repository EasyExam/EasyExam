import React from "react";
import Topic from "./Topic";

class Problem extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <tr>
        <td width="25%">
          {" "}
          <a href="#VerProblema">{this.props.problem.name}</a>
        </td>
        <td width="25%"> {this.props.problem.created_at}</td>
        <td width="25%">
          {" "}
          <Topic topics={this.props.problem.topics} />{" "}
        </td>
        <td width="25%"> {this.props.problem.author}</td>
      </tr>
    );
  }
}

export default Problem;
