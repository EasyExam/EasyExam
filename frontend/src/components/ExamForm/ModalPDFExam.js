import React from "react";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import PreviewProblemButton from "./PreviewProblemButton";

class ModalPDFExam extends React.Component {
  constructor(props) {
    super(props);
    this.handleClose = this.handleClose.bind(this);
    this.getPreview = this.getPreview.bind(this);
    this.state = {
      show: false,
    };
  }
  handleClose() {
    this.setState({ show: false });
  }

  getPreview(event) {
    event.preventDefault();
    this.setState({ show: true });
    const url = `/api/problems/${this.props.uuid}/pdf/`;
    fetch(url, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${localStorage.getItem("token")}`,
      },
    })
      .then((res) => res.blob())
      .then((blob) => {
        let preview_url = URL.createObjectURL(blob);
        this.setState({ url: preview_url });
      });
  }
  render() {
    return (
      <>
        <PreviewProblemButton onClick={this.getPreview} />
        <Modal show={this.state.show} onHide={this.handleClose} size="lg">
          <Modal.Header closeButton>
            <Modal.Title>
              Previsualización :{this.props.problemName}{" "}
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <div>
              <embed
                src={this.state.url + "#toolbar=0"}
                frameBorder="0"
                width="100%"
                height="400px"
              ></embed>
            </div>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleClose}>
              Cerrar
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}
export default ModalPDFExam;
