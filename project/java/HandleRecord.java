package None;

import java.util.List;
import lombok.*;






/**
  A base class for handle-data classes that represent a handle record in the same way as in the REST (json) API of a handle server.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HandleRecord  {

  private ZonedDateTime timestamp;
  private Integer ttl;
  private String type;

}
