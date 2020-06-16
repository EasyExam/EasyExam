import React from "react";
import { Link } from "react-router-dom";
import { Container, Button, Row, Col } from "react-bootstrap";
import ExamList from "./ExamList";

class Exams extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const createExam = (
      <Link to="/exam/create">
        <Button
          variant="primary"
          size="lg"
          block
          style={{ marginTop: "15px", marginBottom: "15px" }}
        >
          Nuevo examen
        </Button>
      </Link>
    );
    return (
      <Container>
        <Row style={{ marginTop: "20px" }}>
          <Col>
            <h1>Mis Exámenes</h1>
            <ExamList />
            {createExam}
          </Col>
        </Row>
      </Container>
    );
  }
}
export default Exams;
