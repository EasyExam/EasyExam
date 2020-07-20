import React from "react";
import { Button, Col, Form, Row } from "react-bootstrap";
import { Plus } from "react-bootstrap-icons";

class AddProblemButton extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <>
        <Form.Group as={Row}>
          <Col>
            <Button
              variant="primary"
              onClick={this.props.addProblem}
              style={{ marginRight: "5px" }}
              block
            >
              <Plus /> Añadir pregunta
            </Button>
          </Col>
        </Form.Group>
      </>
    );
  }
}

export default AddProblemButton;
